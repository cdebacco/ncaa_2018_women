#!/bin/bash

dataDIR=../WDataFiles


for year in {1998..2017}
do
    awk -F, -vyear=$year '($1==year){print $3,$5,1}' $dataDIR/WRegularSeasonCompactResults.csv > $dataDIR/WRegularSeasonCompactResults_$year.csv
    awk -F, -vyear=$year '($1==year){print $3,$5,1}' $dataDIR/WNCAATourneyCompactResults.csv > $dataDIR/WNCAATourneyCompactResults_$year.csv
done


