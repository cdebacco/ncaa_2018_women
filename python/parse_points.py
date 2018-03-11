#!/usr/bin/python

from __future__ import print_function
import numpy as np
import pandas as pd
import tools as tl
import networkx as nx
def to_undirected(G):
    """
    Transform a graph from directed to undirected so that w_ij(undirected)=w_ij(directed)+w_ji(directed)
    """
    UG=nx.Graph()
    UG.add_nodes_from(G)
    for u,v,d in G.edges(data=True):
        if(u!=v):
            if(UG.has_edge(v,u)):UG[v][u]['weight']+=G[u][v]['weight']
            else: UG.add_edge(u,v,weight=G[u][v]['weight'])
        else:   UG.add_edge(u,v,weight=G[u][v]['weight'])#+G[v][u]['weight']) 
    return UG

def compute_comparison_matrix(inadjacency,alpha=1):

    G=tl.build_graph_from_adjacency(inadjacency)

    nodes=list(G.nodes(data=False))
    edges=list(G.edges(data=True))
    N=G.number_of_nodes()
    S=np.zeros((N, N))

    G_und=to_undirected(G);
    for i in range(N):
        u=nodes[i]
        neigh_u=set(G_und.neighbors(u))
        for j in range(i+1,N):
            v=nodes[j]

            '''
            Scontro diretto (i,j)
            '''
            if v in neigh_u: 
                if (u,v) in edges: w_uv=G[u][v]['weight']
                else:w_uv=0
                if (v,u) in edges: w_vu=G[v][u]['weight']
                else:w_vu=0
                S[i,j]+=w_uv*alpha
                S[j,i]+=w_vu*alpha

            '''
            Scontro indiretto (i,k), (j,k)
            '''
            neigh_v=set(G_und.neighbors(v))

            neigh_intersection=list(neigh_u.intersection(neigh_v))

            k_len=float(len(neigh_intersection))
            for k in neigh_intersection:
                q=nodes.index(k)
                if (u,q) in edges: w_uq=G[u][q]['weight']
                else:w_uq=0
                if (q,u) in edges: w_qu=G[q][u]['weight']
                else:w_qu=0
                
                if (v,q) in edges: w_vq=G[v][q]['weight']
                else:w_vq=0
                if (q,v) in edges: w_qv=G[q][v]['weight']
                else:w_qv=0

                siq=(w_uq-w_qu)
                sjq=(w_vq-w_qv)

                S[i,j]+=(1-alpha)*(siq-sjq)/k_len
                S[j,i]+=(1-alpha)*(sjq-siq)/k_len

    return S,nodes

def pointcompare(points1, points2, overtime, norm='sum', factor=1000):
    """
    Dal risultato della partita ci da un numero nell'intervallo [0,factor] che usiamo per fare il train
    """
#   print("Overtime = ", overtime)


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


