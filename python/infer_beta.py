'''
Infer best beta such that it optimizes the desiderata
'''

from __future__ import print_function
import scipy.optimize as opt
import cost_function as cf

seasons=list(range(1998,2018))
rank_type='SpringRank'
epsilon=0.00001

# ---------------------- Cycle over Parameters -------------------

for season_id in seasons:

	outfile='../WDataFiles/WRegularSeasonCompactResults_'+str(season_id)+'_'+rank_type+'_beta.dat'
	outf=open(outfile,'w')

	bounds_beta=[(0,10)]
	beta0=2

	ARGS=(season_id,rank_type,epsilon) #epsilon regolarizza perche la loss est logaritmica e non vogliamo divergenze

	beta,f,d=opt.fmin_l_bfgs_b(cf.evaluation, beta0, fprime=None, args=ARGS, approx_grad=1, bounds=bounds_beta, epsilon=1e-06, iprint=0,callback=None) 

	acc,M=cf.accuracy(season_id,rank_type,beta)

	print(season_id,beta,f,acc,M,file=outf)

	outf.close()

	print('Outfile:',outfile)






