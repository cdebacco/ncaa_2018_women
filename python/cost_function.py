'''
Function needed to be optimized for final evaluation
'''
import pandas as pd
import numpy as np

thresbig=1e6

def evaluation(beta,*ARGS):

    L=0.;   # Initial cost function
    season_id=ARGS[0] # season id
    rank_type=ARGS[1]
    epsilon=ARGS[2]
    losstype=ARGS[3]
    
    df_rank=pd.read_csv('../WDataFiles/WRegularSeasonCompactResults_'+str(season_id)+'_'+rank_type+'.dat',sep=' ', header=None)
    
    if losstype=='train':df_data=pd.read_csv('../WDataFiles/WRegularSeasonCompactResults_'+str(season_id)+'.csv',sep=' ', header=None)
    elif losstype=='test':df_data=pd.read_csv('../WDataFiles/WTourney_'+str(season_id)+'.csv',sep=' ', header=None)

    rank= df_rank.set_index(0).to_dict()[1]

    M=len(df_data)

    for idx,rows in df_data.iterrows():

        Wteam=rows[0]
        Lteam=rows[1]

        p_ij=1./(epsilon+1.+np.exp(-2.*beta*(rank[Wteam]-rank[Lteam])))

        L-=np.log(p_ij)
    
    print(-L/float(M),beta)

    outvalue=L/float(M)
    if outvalue>thresbig: raise SystemExit("Loss is bigger than admitted threshold: L = "+str(outvalue)+" > "+str(thresbig))

    return outvalue



def accuracy(season_id,rank_type,beta):
    '''
    Count number of well predicted match outcomes
    '''
    acc=0.
    df_rank=pd.read_csv('../WDataFiles/WRegularSeasonCompactResults_'+str(season_id)+'_'+rank_type+'.dat',sep=' ', header=None)
    df_data=pd.read_csv('../WDataFiles/WRegularSeasonCompactResults_'+str(season_id)+'.csv',sep=' ', header=None)

    rank= df_rank.set_index(0).to_dict()[1]

    M=len(df_data)

    for idx,rows in df_data.iterrows():

        Wteam=rows[0]
        Lteam=rows[1]

        if rank[Wteam]>=rank[Lteam]:acc+=1
        
    return acc,M