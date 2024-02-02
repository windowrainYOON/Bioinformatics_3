## AF로 예측된 protein에 ligand가 어디에 붙을 지 예측할 때, docking simulation과 homolog-ligand를 기반으로 예측이 가능
## 이를 바탕으로 active site를 예측할 수 있음
## >>pip install biopython
## >>pip install pypdb

from pypdb import *
from Bio import PDB

pdb_id = '5JWR'
pdb_file = get_pdb_file(pdb_id, filetype='pdb', compression=False) # PDB 파일을 불러옴

## Save the pdb file
fo = open('./%s.pdb'%pdb_id, 'w') # 불러온 PDB 파일을 저장할 파일을 생성
print(pdb_file, file=fo) # 생성된 파일에 PDB를 넣어줌
fo.close()

print(pdb_file)

parser = PDB.PDBParser() 
structure = parser.get_structure(pdb_id, './%s.pdb'%pdb_id) # PDB id로부터 구조를 받아옴
structure.get_list()

model = structure[0] 
model.get_list()

chain = model['A']
chain.get_list()

res_ = chain[18]
res = chain[(' ', 18, ' ')]

res.resname

ligand = chain['H_PO4'] # error
ligand = chain[('H_PO4', 301, ' ')]

res.get_list()

ca = res['CA']
cb = res['CB']
ca.coord

import numpy as np

def calc_distance(atom1, atom2):
  distance = np.linalg.norm(atom1.coord - atom2.coord)
  return distance

calc_distance(ca, cb)