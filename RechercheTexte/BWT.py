#!/usr/bin/env python
# coding: utf-8
import cProfile
import re
import time
import numpy
def creationMatrice(texte):
    texte="$"+texte
    container=[texte]*len(texte)
    t=time.clock()
    for i in range (len(texte)):
        container[i]=container[i][len(container[i])-i:]+container[i][:len(container[i])-i]
    container.sort(cmp=None, key=None, reverse=False)
#     AffichageColonne(container)
#     SuffixArray(container)
    tt=time.clock()
    return container
    




def SuffixArray(container):
    l=[]
    for i in range (len(container)):
        ligne_tmp=container[i][:(container[i].index("$")+1)]
        l.append(ligne_tmp)


def creationLFMap(texte):
    
    container=creationMatrice(texte)
    LFMap=[]
    for i in range(len(container)):
        ligne_tmp=[container[i][0],container[i][len(container[i])-1]]
        i=0
        for j in range (len(LFMap)):
            i=i+ LFMap[j][1].count(ligne_tmp[1])
        ligne_tmp.append(i)
        LFMap.append(ligne_tmp)
        
    
    
def FMindex(texte):

    container=creationMatrice(texte)


    dicopremier={}
    dicodeuxieme={}
    t=time.clock()

    for i in range(len(container)):
        ligne_tmp=[container[i][0],container[i][len(container[i])-1]]
        if ligne_tmp[0]  in dicopremier:
            dicopremier[ligne_tmp[0]]=dicopremier[ligne_tmp[0]] +1
        else:
            dicopremier[ligne_tmp[0]]=0
        if ligne_tmp[1]  in dicodeuxieme:
            dicodeuxieme[ligne_tmp[1]]=dicodeuxieme[ligne_tmp[1]] +1
        else:
            dicodeuxieme[ligne_tmp[1]]=0
        ligne_tmp[0]=ligne_tmp[0]+str(dicopremier[ligne_tmp[0]])#.insert(1, premier)
        ligne_tmp[1]=ligne_tmp[1]+str(dicodeuxieme[ligne_tmp[1]])#append(deuxieme)
        ligne_tmp.append(len(container)-container[i].index("$")-1)
        container[i]=(ligne_tmp)
    tt=time.clock()

    print tt-t
    return container

def FMindex2(texte):
    t=time.clock()
    container=creationMatrice(texte)
    LFMap=[]
    for i in range(len(container)):
        ligne_tmp=[container[i][0],container[i][len(container[i])-1]]
        premier=0
        deuxieme=0
        for j in range (len(LFMap)):
            premier=premier+ LFMap[j][0].count(ligne_tmp[0])
            deuxieme=deuxieme+ LFMap[j][1].count(ligne_tmp[1])
        ligne_tmp[0]=ligne_tmp[0]+str(premier)#.insert(1, premier)
        ligne_tmp[1]=ligne_tmp[1]+str(deuxieme)#append(deuxieme)
        ligne_tmp.append(len(container)-container[i].index("$")-1)

        LFMap.append(ligne_tmp)
        
    tt=time.clock()
    print tt-t
    return LFMap
def Recherche(texte,motif):
    LFMap=FMindex(texte)
#     AffichageColonne(LFMap)
    actuel=motif[len(motif)-1]
    suivant=motif[len(motif)-2]
    
    F=[]
    L=[]
    SA=[]
    t=time.clock()


    ensemble=[]
#     F=[LFMap for i in range (len(LFMap))][0]

    for j in range(len(LFMap)):
        F.append(LFMap[j][0])
        L.append(LFMap[j][1])

        SA.append(LFMap[j][2])
        if len(motif)<2 and actuel == L[j][0]:
            ensemble.append(F[j])
            #motif=motif[0:len(motif)-1]
        elif (actuel == F[j][0])  and (suivant == L[j][0]):
            ensemble.append(L[j])
            
    if len(motif)<2 and actuel in L[:][0]:
        p=L[:][0]
#     print "ensemble" 
#     print ensemble
#     #motif=motif[0:len(motif)-1]
#     print "motif"
#     print motif

    for i in reversed(range(len(motif)-2)):

        if len(ensemble)!=0:
            actuel=motif[i]
#             print actuel+"actuel"
            junior=[]
            for k in range(len(ensemble)):
                #print k
#                 print ensemble
#                 #print L[F.index(ensemble[k])]
#                 #print F[k][0]
#                 print L[F.index(ensemble[k])][0]
                if actuel== L[F.index(ensemble[k])][0]:
                    
                    junior.append(L[F.index(ensemble[k])])

                    
   

        if len(junior)>0:
            ensemble=junior

        #print i 
    tt=time.clock()

    print tt-t
    for l in range(len(ensemble)):
        print "Resultat"
        print SA[F.index(ensemble[l])] 
    print len(ensemble) 
    
             

        
f= open("human_seq.fa","r").read()
t1=time.clock()
# Recherche(f,"TTTT")
t2=time.clock()
print t2-t1
cProfile.run('Recherche(f,"TTTT")')