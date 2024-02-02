# Bioinformatics_3
initial commit

기본 가정 : 두 단백질이 서열이 비슷하면 그 구조도 비슷할 것
query sequence -> template detection -> sequence alignment -> moedl building & refinment
서열 정렬하기!
+ "Blosum matrix"
  + 두 아미노산 간의 서열 유사도를 점수로 표현한 blot
+ "Coevolution 기반 단백질 컨택 예측"
  + multiple sequence alignment, residue pair를 비교
  + 진화에 의해 residue가 바뀔 때 residue pair가 동시에 바귀는 경우가 있는데, 이러한 관계를 coevoluation이라고 함


RUNNING Alphafold2
Docker 환경 필요
git clone [alphs fold git page]

...
>>cd docker
>>python3 docker/run_docker.py\
...

alphafold2 : coevolution 기반의 단백질 예측
conda install -c conda-forge pymol-open-source
brew install brewsci/bio/pymol
run pymol


구조 비교 계산
pymol에서 두개 PDB를 다 열어줌
구조 alignment (action -> alogn)

RMSD : 두 분자 간의 차이를 pymol이 자동으로 계산해줌, EGFR정도의 분자의 경우 2보다 작으면 높은 유사도를 갖는다고 생각, 값이 커지면 커질 수록 낮은 유사도
SCOTIN, SCOTIN delta IDR은 20.160
hSCOTIN, mSCOTIN은 12.643

Multimer
서로 다른 두 sequence를 input으로 넣어주되, seq1:seq2을 넣어주고 돌려줌

pymol
^우클릭 + ^휠 클릭으로 원자 두개를 성택시 거리 계산 가능, 세개 선택 시 각도 계산 가


RMSD는 두 원자 간의 편차 평균인데, 이상치에 대해 예민한 경향을 가짐
여러 측정법이 있지만, 오늘 배울 것은 TM-SCORE (이상치에 대해 예민하지 않음)
>>>conda install bioconda::tmalign
아래 명령어를 pymol 창에 입력
tmalign name1, name2 

cealign(combinatorial expension alignment) : 서열 상동성은 없지만 구조적으로 우사한 두 단백질의 겹침 구조를 확인할 
super name1, name2

global optimization
구조 공간에서 가장 낮은 에너지를 가지는 구조를 찾는 것
local minimum을 방지ㅏ기 위해서 확률 기반 알고리즘을 사용함

Autodock Vina를 이용해 docking simulation을 실습

알고리즘 -> self-attention을 사용

protein protein interactio prepdiction byn
=> physiclal interaction

1. PPI woth alphafold
2. drug efficiency prediction


EVcoupling -> domain-domain interaction prediction

predicted DockQ score : 서버가 있어야 예측해볼 수 있음

Accurate prediction of protein-Nucleic acid complexes using RoseTTAFoldNA

Clustering predicted structures at the scale of the known protein universe
=> unexplored cluster에 대한 얘기를 할 예정
Deep FRI (Depp Functional Residue Identification) : Predicted pockets, GO, EC numb을 확인하는 프로젝트

Protein design

DockQ score
0 < x <  0.23 : Incorrect
0.23 < x <  0.49 : Acceptable quality
0.49 < x <  0.8.80 : Meium quality
x >  0.8.80 : High quality


Improved prediction of protein-protein interactions using AplphaFold2

Coevolution : Organism -> proteome -> MSA creation -> MSA block diagnulation (MSA pairing with spquences) sturcture of predictiton of complexes
PPI network

DeepConv DTI: Prediction of drug-target interactions via deep learning with conveolution on portien sequences


DockQ 이용법
DockQ는 protein-protein interaction 예측 model과 실제 protein-protein interaction model 간의 예측 정확도를 비교하는 툴

git clone https://github.com/bjornwallner/DockQ/
pip install biopython
python DockQ.py ./examples/model.pdb ./examples/native.pdb

---
---

Protein의 구조변화를 예측하는 방법


train on human curated database : ClinVar
train on the weak labels : CADD
unsupervised approaches : EVmutation, (CECS score : Cost of coupling, Coupling number)
  interface, rest of surface, protein core 나누어서 분석 -> interface에 더 많은 disease mutant가 발견
exploit protein structures : 


AlphaMissense : protein-protein별로 mutation과 pathogenesity 등을 계산해 놓은 파일이 있음
양이 엄청 많기 때문에 한줄 씩 읽어내려가는 코드가 필요함

