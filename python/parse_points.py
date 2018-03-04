#!/usr/bin/python

import numpy as np
import pandas as pd




def pointcompare(points1, points2, overtime, norm='sum', factor=1000):
	"""
	Dal risultato della partita ci da un numero nell'intervallo [0,factor] che usiamo per fare il train
	"""
#	print("Overtime = ", overtime)


	if norm=='vic': return 1

	if int(overtime)>0: 
		val=0;
	else: 
		val=(points1-points2)
		if norm=='sum':
			val/=(points1+points2)
		elif norm=='max':
			val/=max(points1,points2)
		elif norm=='min':
			val/=(min(points1,points2)+0.1) #0.1 to avoid unlikely division by zero
	return (val+1)*factor


if __name__=='__main__':

	df_data=pd.read_csv('../WDataFiles/WRegularSeasonCompactResults.csv')

#    print(df_data['NumOT'])

	# df_data['compare']=df_data.apply(pointcompare,args=(df_data['WScore'],df_data['LScore'],df_data['NumOT']))

	for norm in ['sum','max','min','vic']:

		outf=open('../WDataFiles/WRegularSeasonCompactResults_'+str(norm)+'.csv',"w")
		for idx,line in df_data.iterrows():
			print(
				line['Season'],
				line['WTeamID'],
				line['LTeamID'],
				pointcompare(line['WScore'], line['LScore'], line['NumOT'], norm=norm),
				file=outf
				)
		outf.close()


