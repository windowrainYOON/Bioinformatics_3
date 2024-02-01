from rdkit import Chem
from rdkit.Chem import Allchem ## 어떤 이유에서인지 이 lirary가 없다고 뜬다
from rdkit.Chem import MACCSkeys
from rdkit import DataStructs

m1 = Chem.MolFromSmiles('CC(=O)OC1=CC=CC=C1C(=O)O')
m2 = Chem.MolFromSmiles('CC(C)CC1=CC=C(C=C1)C(C)C(=O)O')

f1 = Allchem.GetMorganFingerprint(m1, 2) ## ECFP와 유사한 알고리즘
f2 = Allchem.GetMorganFingerprint(m1, 2) 

DataStructs.TanimotoSimilarity(f1, f2)

f1 = MACCSkeys.GenMACCSKeys(m1) ## MACCS 알고리즘으로 smiles -> fingerprint로 변환
f2 = MACCSkeys.GenMACCSKeys(m2)

DataStructs.TanimotoSimilarity(f1, f2)