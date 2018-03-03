#!/bin/bash

#Come prima cosa, creiamo un file con le colonne che ci servono:
# Winner, Loser, Vittoria=1
#output: ./WDataFiles/WRegularSeasonCompactResults_$year.csv
cd scripts
bash parse_data.sh



cd ../python/
# Ora calcoliamo il rank
# L'output e` un file da due colonne, con spazi, non virgole
# (teamID, rank)
#./WDataFiles/WRegularSeasonCompactResults_${year}'_SpringRank.csv
python calculate_SpringRank.py 



#Ora calcoliamo la beta (parametro libero analogo alla temperatura)
#che ci da la migliore loss function.

python infer_beta.py 

