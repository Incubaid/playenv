# Capnproto Test
# Installation 
* for installation follow [Installation Guide](http://jparyani.github.io/pycapnp/install.html) 

# Run it 

```python
python3 capnp_test.py
```
# Serialization
```python
company = Company.Company.new_message()
branches = company.init('branches', 1)
#adding maadi branch
maadi = branches[0]
maadi.id = 1
maadi.name = "Maadi"
maadi.email = "maadi@codescalers.com"
phones = maadi.init("phones", 2)
land = phones[0]
land.number = "0200192910"
land.type = "land"
mobile = phones[1]
mobile.number = "0120219201"
mobile.type = "mobile"
maadi.field = "head"
maadi.address = "Cairo, Maadi, street9"
branches
```
# writing to file 
```python
with (open('codescalers.bin', 'w+b')) as f:
    company.write(f)
```
# Reading file and deserialization 
```python

with (open('codescalers.bin', 'r+b')) as f:
    codescalers = Company.Company.read(f)
for branch in codescalers.branches:
    print(branch.name)
    
```
# Experience 
* the api is a bit intuitive and easy to read and understand
