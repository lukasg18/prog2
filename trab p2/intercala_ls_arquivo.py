#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  organiza_arquivos.py
#  
#  
def acumulaverdades(lschaves):# testa se todos os arquivos estão retornando vazio
	oka=True
	okb=False
	for elem in lschaves:
		if elem == float('Inf'):
			oka = False
		else:
			oka= True
		okb = okb or oka
	return okb

#acumulaverdades

def pegamenor(lst): #pega o menor numero da lista
	aux= float(lst[0] )
	for elem in lst:
		if aux > float(elem):
			aux = float(elem)
	return aux
#pega menor

def salva(palavra):
	arquivo = open(("save.txt"),"a")
	arquivo.write(str(palavra)+"\n")
	arquivo.close()
	
def intercalaArquivo(arquivos):
	lschave=[]
	lslinhas=[]
	segura=0
	for elem in arquivos: # jogando a primeira linha de cada arquivo na lista
		lschave.append(float(elem.readline()))
		
	maiorR = float('Inf')
	lstTotal = []

	while acumulaverdades(lschave):
		menor = pegamenor(lschave)
		for ind in range(len(lschave)): #passa por todas os primeiros numeros
			if menor == lschave[ind]: #descobre de qual lista foi retirado o menor elemento
				salva(menor)

				segura = arquivos[ind].readline() # atualiza a lista com o proximo elemento
				
				if segura != "": #confere se o arquivo acabou
					lschave[ind] = float(segura) #
				else:
					lschave[ind] = maiorR #		
	return "OK"


def main():
	doca = open("doca.txt","r")
	docb = open("docb.txt","r")
	docc = open("docc.txt","r")

	print(intercalaArquivo([doca,docb,docc]))
	
	
	doca.close()
	docb.close()
	docc.close()
	return 0

if __name__ == '__main__':
    main()
