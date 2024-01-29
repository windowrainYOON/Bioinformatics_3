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

