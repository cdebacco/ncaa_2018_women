'''
Infer best beta such that it optimizes the desiderata
'''

from __future__ import print_function
import scipy.optimize as opt
import cost_function as cf

seasons=list(range(1998,2018))
rank_type='SpringRank'
epsilon=0.00001
losstype='train' # we use the train set to calculate the best beta

# ---------------------- Cycle over Parameters -------------------

for gamma in [1.0, 0, 0.4, 0.7]:
	for comparetype in ['min','max','sum','vic']:
		for season_id in seasons:

			outfile='../WDataFiles/WRegularSeasonCompactResults_'+str(season_id)+'_'+rank_type+'_'+comparetype+'_g'+str(gamma)+'_beta.dat'
			outf=open(outfile,'w')

			bounds_beta=[(0,10)]
			beta0=1.7

			ARGS=(season_id,rank_type,epsilon,losstype,comparetype,gamma) #epsilon regolarizza perche la loss est logaritmica e non vogliamo divergenze

			beta,f,d=opt.fmin_l_bfgs_b(cf.evaluation, beta0, fprime=None, args=ARGS, approx_grad=1, bounds=bounds_beta, epsilon=1e-06, iprint=0,callback=None) 

			acc,M=cf.accuracy(season_id,rank_type,beta,comparetype,gamma)

			print(season_id,beta[0],f[0],acc,M,file=outf)

			outf.close()

			print('Outfile:',outfile)






