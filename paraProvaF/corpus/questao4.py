#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  questao4.py
#  
#  Copyright 2016 Lucas <lucas@lucas-Inspiron-3421>
#  
import sys
def frequenciaTxt(paramTXT):
	lstPalavras = separaPal(paramTXT)
	dicFreq = {}

	for elem in lstPalavras:
		if elem.lower() in dicFreq:
			dicFreq[elem.lower()] += 1
		else:
			dicFreq[elem.lower()] = 1
			
	return dicFreq
# fim frequencia

def separaPal(paramTXT):
	novaStr = ''
	lstPalavras = []
	lstSeparadores = [" ' ", ' - ' ]

	for elem in paramTXT:
		if elem == ' ' :
			lstPalavras.append(novaStr)
			novaStr = ''
		elif elem in lstSeparadores:
			novaStr += elem
		elif elem.isalnum():
			novaStr+= elem
		else:
			lstPalavras.append(elem)
	if novaStr != '' :
		lstPalavras.append(novaStr)
	return lstPalavras
# fim separaPal

def matrizFreq(arquivo):	
	dic = {}
	strbuffer = ""
	arqOri = open(arquivo,"r")
	#~ arqOri = open(arquivo + "/lstcorpus.txt","r")
	linhaOri = arqOri.readline()
	
	while linhaOri != "": 	
		nomeArq = open(linhaOri[:-1],"r")
		linhaArq = nomeArq.readline()
		
		while linhaArq != "":
			strbuffer += linhaArq + " "   # <<<<  Salvo no strbuffer para q n perca o arquivo
			linhaArq  = nomeArq.readline()
		linhaOri = arqOri.readline()
		
	arqOri.close()
	dic = frequenciaTxt(strbuffer)  #  <<<< trato com o frequencia depois de todos os textos estarem no strbuffer
	return dic
	
def main():
    arquivo  = sys.argv[1]   # <<< por linha de comando
    print(matrizFreq(arquivo))
    return 0

if __name__ == '__main__':
	main()
