#!/usr/bin/env python
# -*- coding: utf-8 -*-

def naif(motif,texte):
	reponse=[]
	for i in range (len(texte)):
		if (motif==texte[i:len(motif)+i]):
			reponse.append(i)
	print reponse


def RK(motif,texte):
	Lmotif=len(motif)
	Ltexte=len(texte)

	motifConverti=conversion(motif)
	motifConverti=hash(motifConverti,10)

	for i in range (Ltexte-Lmotif+1):
		texteConverti=conversion(texte[i:Lmotif+i])
		texteConverti=hash(texteConverti,10)
		if texteConverti==motifConverti:

			if texte[i:Lmotif+i]==motif:
				print "Gagne à la position ",i



def hash(texte, base):
	#for i in range (len(texte)):
	#	texte[i]=texte[i]%base
	#return texte

	texte=int(texte)
	return texte%base


def conversion(texte):
	texteConverti=[]
	for i in range (len(texte)):
		if texte[i]=='a':
			texteConverti.append('1')
		elif texte[i]=='t':
			texteConverti.append('2')
		elif texte[i]=='c':
			texteConverti.append('3')
		elif texte[i]=='g':
			texteConverti.append('4')
		else:
			texteConverti.append('5') #Erreur
	resultat=''
	for i in range (len(texte)):
		resultat=resultat+texteConverti[i]
	return resultat


def KMP(motif,texte):
	motif=motif
	pi=fonctionPrefixe(motif)
	q=0
	rep=0
	for i in range (len(texte)):

		while (q>0 and motif[q]!=texte[i]):
			q=pi[q-1]

		if motif[q]==texte[i]:
			q=q+1
		if q==len(motif):
			rep = rep+1
			print ("Le motif apparait en position", i-len(motif)+1)
			print rep
			q=pi[q-1]
			print q
	print rep/len(motif)
def fonctionPrefixe(motif):
	pi=[]
	for i in range (len(motif)):
		pi.append(0)

	k=0
	for i in range (1,len(motif)):
		while (k>0 and motif[k]!=motif[i]):
			k=pi[k]
		if (motif[k]==motif[i]):
			k=k+1
		pi[i]=k
	print pi
	return pi
f = open("human_seq.fa","r").read()

fonctionPrefixe("ababababca")
KMP ("GAATT",f);
