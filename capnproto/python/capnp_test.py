import capnp
import company_capnp as Company

company = Company.Company.new_message()
branches = company.init('branches', 2)
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

#adding naser city branch

naser_city = branches[1]
naser_city.id = 1
naser_city.name = "Naser City"
naser_city.email = "naser_city@codescalers.com"
phones = naser_city.init("phones", 2)
land = phones[0]
land.number = "0300192910"
land.type = "land"
mobile = phones[1]
mobile.number = "0100219201"
mobile.type = "mobile"
maadi.field = "development"
maadi.address = "Cairo, Naser City, street9"

# writing to file
with (open('codescalers.bin', 'w+b')) as f:
    company.write(f)

#reding the file
with (open('codescalers.bin', 'r+b')) as f:
    codescalers = Company.Company.read(f)

branches_names = ['Maadi', 'Naser City']

for branch in codescalers.branches:
    assert branch.name in branches_names

print("Created and verified")