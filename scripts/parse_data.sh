#!/bin/bash


dataDIR=../WDataFiles


#for year in {1998..2017}
for year in 2018
do
    #awk -F, -vyear=$year '($1==year){print $3,$5,1}' $dataDIR/WNCAATourneyCompactResults.csv > $dataDIR/WNCAATourneyCompactResults_$year.csv
#    awk -v year=$year '($1==year){print $3,$5,1}' $dataDIR/WNCAATourneyCompactResults.csv > $dataDIR/WNCAATourneyCompactResults_$year.csv


    for comparetype in vic # min max sum vic
    do
	#Queste due righe sono equivalenti a comparetype=vic
	#Queste righe prendono il file crudo dato da quelli del contest,
	#quelle non commentate prendono uno gia preanalizzato con lo script parse_points.py
	#	awk -F, -vyear=$year '($1==year){print $3,$5,1}' $dataDIR/WRegularSeasonCompactResults.csv > $dataDIR/WRegularSeasonCompactResults_$year.csv

	#awk -vyear=$year '($1==year){print $2,$3,$4}' $dataDIR/WRegularSeasonCompactResults_$comparetype.csv > $dataDIR/WRegularSeasonCompactResults_${year}_${comparetype}.csv
	awk -v  year=$year '($1==year){print $2,$3,$4}' $dataDIR/RegularSeasonCompactResults_$comparetype.csv > $dataDIR/RegularSeasonCompactResults_${year}_${comparetype}.csv

    done
done

mkdir -p $dataDIR/Results
