# dnsmasq alternative
This is a set of tools aimed to replace dnsmasq and other stuff related to network.

This was made in El Gouna, using Ubuntu 16.04.

# Setup the Network

All you need is a bridge which will contains wireless card and ethernet card and enable the router feature.

First, install the tools: `apt-get install bridge-utils nftables`

remove existing nftables config
```
rm -f /etc/nftables.conf
```

Simply add a bridge to the network configuration (`/etc/network/interfaces`):
```
auto br0
iface br0 inet static
  address 192.168.86.254
  netmask 255.255.255.0
  bridge_ports eno1

```

Add this to `/etc/rc.local` to enable routing:
```
echo 1 > /proc/sys/net/ipv4/ip_forward
nft -f /etc/nftables.conf
```

Note: replace `eno1` with your local interface of course. You can (need) *reboot* now to make sur all is applied.

# The basics

Clone this repo on the router, then to make it easy, make a symlink to access it in a safe way
(to follow this README correctly):
```
cd /opt && git clone https://github.com/0-complexity/playenv
ln -s /opt/playenv/dnsmasq-alt .
```

And install jumpscale8 which will be needed:
```
cd /tmp/
apt-get install -y python3.5 curl
curl -k https://raw.githubusercontent.com/Jumpscale/jumpscale_core8/master/install/install.sh > install.sh;bash install.sh
```

It's useful to run every daemons in a tmux session to be able to watch them easier.

# DNS

The DNS server/forwarder/filter is based on dnslib.

- Install [dnslib](https://github.com/paulchakravarti/dnslib): `pip3 install dnslib`
- Start the DNS server (in a tmux): `jspython /opt/dnsmasq-alt/dns-server.py`

For now, this dns-code is a dns-forwarder with cache (using `j.core.db`) and hit count.

You can get some statistics with `/opt/dnsmasq-alt/dns-stats.py` script.

# Wifi dongle

In El Gouna, we used a `rtl871x` based usb-dongle.
Like most of realtek dongle, some patch need to be applied.

The configuration of hostapd is stored in `wifi-special-dongle/hostapd.conf`
and there is a bash script used to install drivers, compile and patch hostapd to make it works.

You can run it: `cd /opt/dnsmasq-alt/wifi-special-dongle/ && bash -x setup.sh`

For information, dongle usb ID is `0bda:818b`.

Change the interface name in the configuration file: `/opt/dnsmasq-alt/wifi-special-dongle/hostapd.conf`

Run hostapd (in a tmux): `/opt/netpoc/hostapd-2.5/hostapd/hostapd /opt/dnsmasq-alt/wifi-special-dongle/hostapd.conf`

Note: you will need to change the wireless interface in the config file.
Note2: it's possible that the interface doesn't join the bridge itself, if it's the case
(`brctl show` will tell you if the interface is plugged in br0), add it manually: `brctl addif br0 INTERFACE`

# HTTP/HTTPS transparent proxy

Some http(s) filtering was made with [mitmproxy](https://github.com/mitmproxy/mitmproxy).

IMPORTANT: check that python points to python3 (if not change the symlink)


- Install the dependancies: `apt-get install python3-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev`
- Pre-install some conflicting dependancies: `pip3 install cffi`
- Install last version: `pip3 install git+https://github.com/mitmproxy/mitmproxy.git`
- Start the server (in a tmux): `mitmdump -T -d -p 8443 -s /opt/dnsmasq-alt/http-filter.py`

The `-T` option is needed when running a transparent proxy. If you want to run a proxy reachable with an explicit
proxy setting, you need to remove the `-T` option. To make it cohabit, you can run 2 instance on separated port:
- `mitmdump -T -d -p 8443 -s /opt/dnsmasq-alt/http-filter.py` # Transparent mode
- `mitmdump -d -p 4040 -s /opt/dnsmasq-alt/http-filter.py` # Proxy mode

If you need to allow some hosts (eg: zoom), you can add do:
- `mitmdump -T -d -p 8443 -s /opt/dnsmasq-alt/http-filter.py --ignore zoom.us`

The `--ignore` option accepts regex.


`http-filter.py` is in this repository and is used to make some content filtering.
When the proxy is running, go to [mitm.it](http://mitm.it) special url and install the certitifcate.

You can get some statistics via the `/opt/dnsmasq-alt/http-stats.py` script.

# DHCP

For now, we still use the mainstream dhcp server. This gonna change. But for now...

- Install the dhcp server: `apt-get install isc-dhcp-server`
- Edit `/etc/dhcp/dhcpd.conf` and add this block at the end:
```
subnet 192.168.86.0 netmask 255.255.255.0 {
  range 192.168.86.100 192.168.86.200;
  option domain-name-servers 192.168.86.254;
  option subnet-mask 255.255.255.0;
  option routers 192.168.86.254;
  option broadcast-address 192.168.86.255;
  default-lease-time 600;
  max-lease-time 7200;
}
```
- Apply some fix on the config: `sed -i 's/^option domain-name/#option domain-name/g' /etc/dhcp/dhcpd.conf`
- Set interface to startup options: `sed -i 's/INTERFACES=""/INTERFACES="br0"/g' /etc/default/isc-dhcp-server`
- Restart the server: `/etc/init.d/isc-dhcp-server restart`

# Firewall rules

In the PoC used in El Gouna, the firewall was setup using nftables.
The ruleset can be found on the `nftables.conf` file.

This firewall rules makes transparent redirections and some basic filtering.
Apply it at the end to make the redirections works when all the proxies are set up.

- Copy the firewall rules file to the system one: `cp /opt/dnsmasq-alt/nftables.conf /etc/`
- Set the interface correctly: `sed -i s/eth1/WAN_INTERFACE/g /etc/nftables.conf` (adapt WAN_INTERFACE)
- Run the rules: `nft -f /etc/nftables.conf`

You can check if it's applied with: `nft list ruleset`
