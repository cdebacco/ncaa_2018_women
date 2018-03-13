#!/bin/bash

#Come prima cosa, creiamo un file con la coparazione tra squadre che ci interessa
#Abbiamo varie modalita`, usiamo un file per ognuna.
cd python
python parse_points.py

# Poi riorganizziamo il formato in modo che il programma dello springrank possa leggerlo
# Winner, Loser, Comparison
#output: ../WDataFiles/WRegularSeasonCompactResults_$year.csv
cd ../scripts
bash parse_data.sh



cd ../python/
# Ora calcoliamo il rank
# L'output e` un file da due colonne, con spazi, non virgole
# (teamID, rank)
#../WDataFiles/WRegularSeasonCompactResults_${year}'_SpringRank.csv
python calculate_SpringRank.py 

#Ora calcoliamo la beta (parametro libero analogo alla temperatura)
#che ci da la migliore loss function.
#Il formato est una sola riga
# (seasonID, beta, train loss, train #correct, train #total)
# L'output est in
# ../WDataFiles/WRegularSeasonCompactResults_${year}'_SpringRank_beta.csv
python infer_beta.py 

#Ora calcoliamo la test loss
#L'output ha il formato
# (year, beta, loss)
#Nome file:
# ../WDataFiles/testlosses.txt
 python test_loss.py
#Possiamo anche scegliere noi la beta da applicare a tutti gli anni
# python test_loss.py 1.9
