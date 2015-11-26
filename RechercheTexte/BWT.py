def creationMatrice(texte):
    container=[]
    for i in range (len(texte)+1):
        container.append("$"+texte)
    decale(container)
    container.sort(cmp=None, key=None, reverse=False)
    AffichageColonne(container)
    SuffixArray(container)
    return container
    
        
def decale(container):
    #Décale les motifs
    for i in range (len(container)):
        ligne_tmp=container[i][len(container[i])-i:]+container[i][:len(container[i])-i]
        container[i]=ligne_tmp



def SuffixArray(container):
    l=[]
    for i in range (len(container)):
        ligne_tmp=container[i][:(container[i].index("$")+1)]
        l.append(ligne_tmp)

    AffichageColonne(l)

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
        
    AffichageColonne(LFMap) 
    
    
def FMindex(texte):
    
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
        

    return LFMap

def Recherche(texte,motif):
    LFMap=FMindex(texte)
    AffichageColonne(LFMap)
    actuel=motif[len(motif)-1]
    suivant=motif[len(motif)-2]
    print actuel
    
    F=[]
    L=[]
    SA=[]
    
    for i in range (len(LFMap)):
        F.append(LFMap[i][0])
        L.append(LFMap[i][1])

        SA.append(LFMap[i][2])
    ensemble=[]

    for j in range(len(L)):
        if len(motif)<2 and actuel == L[j][0]:
            ensemble.append(F[j])
            #motif=motif[0:len(motif)-1]
        elif (actuel == F[j][0])  and (suivant == L[j][0]):
            ensemble.append(L[j])
    print ensemble
    #motif=motif[0:len(motif)-1]

    print motif
    for i in reversed(range(len(motif))):

        if len(ensemble)!=0:
            actuel=motif[i]
            print actuel+"actuel"
            junior=[]
            for k in range(len(ensemble)):
                print k
                print ensemble
                print L[F.index(ensemble[k])]
                print F[k][0]
                if actuel== L[F.index(ensemble[k])][0]:
                    
                    junior.append(L[F.index(ensemble[k])])
                    print junior
   

            if len(junior)>0:
                ensemble=junior

        print i 
    for l in range(len(ensemble)):
        print "Resultat"
        print SA[F.index(ensemble[l])]  
    
             
def AffichageColonne(container):
    for i in range(len(container)):
        print container[i]
Recherche("couaccou","cou")
