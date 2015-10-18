#!/usr/bin/env python
# -*- coding: utf-8 -*-

def naif(motif,texte):
	reponse=[]
	for i in range (len(texte)):
		if (motif==texte[i:len(motif)+i]):
			reponse.append(i)
	


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
	pi=fonctionPrefixe(motif)
	q=0
	for i in range (len(texte)):
		while (q>0 and motif[q+1]!=texte[i]):
			q=pi[q]
		if motif[q]==texte[i]:
			q=q+1
		if q==len(motif):
			print ("Le motif apparait en position", i-len(motif)+1)
			q=pi[q-1]

def fonctionPrefixe(motif):
	pi=[]
	for i in range (len(motif)):
		pi.append(0)

	k=0
	for i in range (2,len(motif)):
		while (k>0 and motif[k+1]!=motif[q]):
			k=pi[k]
		if (motif[k+1]==motif[q]):
			k=k+1
		pi[q]=k

	return pi

KMP ("a","atca");
