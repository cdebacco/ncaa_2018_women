#!/usr/bin/python


import pandas as pd
import numpy as np
import cost_function as cf
import sys

seasons=list(range(1998,2018))
rank_type='SpringRank'
epsilon=0.00001
losstype='test'
beta0=None
if len(sys.argv)==2:
	beta0=np.float64(sys.argv[1])


for gamma in [1.0, 0, 0.4, 0.7]:
	for comparetype in ['min','max','sum','vic']:
		print('comparetype:',comparetype)

		outname='../WDataFiles/Results/testlosses_'+str(comparetype)+'_g'+str(gamma)+'.txt' if beta0==None else '../WDataFiles/Results/testlosses_beta'+str(beta0)+'_'+str(comparetype)+'_g'+str(gamma)+'.txt'
		outf=open(outname,"w")
		averageloss=0
		averagebeta=0
		for season_id in seasons:

			#Prendiamo i rank
			# df_rank=pd.read_csv('../WDataFiles/WRegularSeasonCompactResults_'+str(season_id)+'_'+rank_type+'.dat',sep=' ', header=None)
			# rank= df_rank.set_index(0).to_dict()[1]


			#Prendiamo beta
			if beta0==None:
				df_beta=pd.read_csv('../WDataFiles/WRegularSeasonCompactResults_'+str(season_id)+'_'+rank_type+'_'+comparetype+'_g'+str(gamma)+'_beta.dat',sep=' ', header=None)
				beta=df_beta.iloc[0][1]
			else: beta=beta0

			testloss=cf.evaluation(beta, season_id, rank_type, epsilon, losstype, comparetype, gamma)


			print(season_id, beta, testloss,file=outf)
			averageloss+=testloss
			averagebeta+=beta

		averageloss/=len(seasons)
		averagebeta/=len(seasons)
		print("average loss = ",averageloss)
		print("average beta = ",averagebeta)
		outf.close()


