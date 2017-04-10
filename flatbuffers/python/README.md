# Flatbuffers Test

# Installation 
* for installation follow [Building Instruction](https://google.github.io/flatbuffers/flatbuffers_guide_building.html) 
* then you need to generate the schema to the language of you choice
# Serialization in flatbuffers
this an example for adding a branch to the company
 
```python
  builder = flatbuffers.Builder(0)
  branch_name = builder.CreateString('Maadi')
  branch_address = builder.CreateString('Cairo, Maadi, street9')
  Branch.BranchStart(builder)
  Branch.BranchAddName(builder, branch_name)
  Branch.BranchAddAddress(builder, branch_address)
  Branch.BranchAddField(builder, Field.Field().Head)
  maadi = Branch.BranchEnd(builder)

  branch_name = builder.CreateString('Naser City')
  branch_address = builder.CreateString('Cairo, Naser City, abbas street')
  Branch.BranchStart(builder)
  Branch.BranchAddName(builder, branch_name)
  Branch.BranchAddAddress(builder, branch_address)
  Branch.BranchAddField(builder, Field.Field().Development)
  naser_city = Branch.BranchEnd(builder)

  Comp.CompanyStartBranchesVector(builder, 1)
  builder.PrependUOffsetTRelative(maadi)
  branches = builder.EndVector(1)
```

# Example for deserialization 

```python
  company = Comp.Company.GetRootAsCompany(buf, 0)
  assert company.Name().decode('utf-8') == 'Codescalers'
  print(company_name = company.Name().decode('utf-8'))
  for i in range(company.BranchesLength()):
      print(company.Branches(i).Name().decode('utf-8'))

```
# Run it
 
```python
python3 test_builder.py
```

# Experience 
*the api is a bit tricky and you need extra steps to get it to work compared to `capnproto`
