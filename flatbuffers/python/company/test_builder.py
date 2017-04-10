#!/usr/bin/python
# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# To run this file, use `python_sample.sh`.

# Append paths to the `flatbuffers` and `MyGame` modules. This is necessary
# to facilitate executing this script in the `samples` folder, and to root
# folder (where it gets placed when using `cmake`).
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../python'))

import flatbuffers
import Company.Sample.Company as Comp
import Company.Sample.Branch as Branch
import Company.Sample.Field as Field
# from Company.Sample import *

# Example of how to use FlatBuffers to create and read binary buffers.

def main():
  builder = flatbuffers.Builder(0)
  #Add Branches
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

  Comp.CompanyStartBranchesVector(builder, 2)
  builder.PrependUOffsetTRelative(naser_city)
  builder.PrependUOffsetTRelative(maadi)
  branches = builder.EndVector(2)


  # Serialize the FlatBuffer data.
  company_name = builder.CreateString('Codescalers')
  Comp.CompanyStart(builder)
  Comp.CompanyAddBranches(builder, branches)
  Comp.CompanyAddName(builder, company_name)
  codescalers = Comp.CompanyEnd(builder)
  builder.Finish(codescalers)

  # We now have a FlatBuffer that we could store on disk or send over a network.

  # ...Saving to file or sending over a network code goes here...

  # Instead, we are going to access this buffer right away (as if we just
  # received it).

  buf = builder.Output()

  # Note: We use `0` for the offset here, since we got the data using the
  # `builder.Output()` method. This simulates the data you would store/receive
  # in your FlatBuffer. If you wanted to read from the `builder.Bytes` directly,
  # you would need to pass in the offset of `builder.Head()`, as the builder
  # actually constructs the buffer backwards.
  company = Comp.Company.GetRootAsCompany(buf, 0)
  assert company.Name().decode('utf-8') == 'Codescalers'
  branches = ['Maadi', 'Naser City']
  for i in range(company.BranchesLength()):
      assert company.Branches(i).Name().decode('utf-8') == branches[i]

  print ('The FlatBuffer was successfully created and verified!')

if __name__ == '__main__':
  main()
