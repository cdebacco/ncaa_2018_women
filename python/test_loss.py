#!/usr/bin/python


import pandas as pd
import numpy as np
import cost_function as cf

seasons=list(range(1998,1999))
rank_type='SpringRank'
#epsilon=0.00001

for season_id in seasons:

	#Prendiamo i rank
	# df_rank=pd.read_csv('../WDataFiles/WRegularSeasonCompactResults_'+str(season_id)+'_'+rank_type+'.dat',sep=' ', header=None)
	# rank= df_rank.set_index(0).to_dict()[1]


	#Prendiamo beta
	df_beta=pd.read_csv('../WDataFiles/WRegularSeasonCompactResults_'+str(season_id)+'_'+rank_type+'_beta.dat',sep=' ', header=None)
	beta=df_beta.iloc[0][1]

	#load test set
	df_test=pd.read_csv('../WDataFiles/WTourneyCompactResults_'+str(season_id)+'.csv',sep=' ', header=None)



