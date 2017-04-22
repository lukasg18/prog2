#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bibliVet.py
#  
#  Copyright 2016 Lucas <lucas@lucas-Inspiron-3421>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import math

def cosseno(lstv,lstu):
	cos,auxv,auxu = 0.0, 0.0, 0.0

	if(len(lstu) != len(lstv)):
		return None
	else:
		for i in range(len(lstv)):
			cos = cos + (lstv[i] * lstu[i])                         # (1x5) + (2x6)
			auxv,auxu = auxv + lstv[i]**2, auxu + lstu[i]**2        # 1² + 2² 
		auxv,auxu = auxv**(1/2.0), auxu**(1/2.0)                    # raiz de 14 , raiz de 62              
		cos = cos / (auxv * auxu)           # 20 / raiz 14 X raiz 62
		#cos = math.acos(cos)                #arcos(cos)
		#cos = math.degrees(cos)             # transformando em graus
		
	return float( '%.2f' % ( cos ) )
		
def matrizCos(lstv):
	lstu = []
	for i in range(len(lstv)):
		linha = []
		for j in range(len(lstv)):
			linha.append(float(cosseno(lstv[i],lstv[j])))
		lstu.append(linha)
	return lstu

def compoeEV(endereco):
	linhanome=[]
	linhavalor=[]
	arqOri = open(endereco + "/bdev.txt","r")
	linhaOri = arqOri.readline()
	
	while linhaOri != "": 
		nomeArq = open(endereco+"/"+linhaOri[:-1],"r")
		linhaArq = nomeArq.readline()
		
		while linhaArq != "":
			(nome,valor) = linhaArq.split(",")
			if(nome not in linhanome):
				linhanome.append(nome)
			linhaArq = nomeArq.readline()
		#fim while
		linhaOri = arqOri.readline()
	#fim while
	fazInsercao(linhanome)
	return linhanome
#fim compoeEV

def salvaEV(lst):
	arquivo = open("dimev.txt","a")
	for elem in range(len(lst)):
		arquivo.write(lst[elem]+"\n") 
	arquivo.close() 
#fim salvaEV

def carregaEV(nome):
	lst = []
	arquivo = open(nome,"r")
	linha = arquivo.readline()
	while linha != "":
		lst.append(linha[:-1])
		linha = arquivo.readline()
	return lst
#fim carregaEV

def matrizEV(endereco):
	lst = compoeEV(endereco)
	matvalor = []
	linhavalor = []
	linhanome = []
	auxvalor = []
	j = 0
	aux = 0
	i = 0
	
	arqOri = open(endereco + "/bdev.txt","r")
	linhaOri = arqOri.readline()
	
	while linhaOri != "": 
		nomeArq = open(endereco+"/"+linhaOri[:-1],"r")
		linhaArq = nomeArq.readline()
		linhavalor = []
		linhanome=[]
		auxvalor=[]
		
		while linhaArq != "":
			(nome,valor) = linhaArq.split(",")
			linhanome.append(nome)
			linhavalor.append(float(valor))
			linhaArq = nomeArq.readline()
		#fim while
		aux = 0
		i = 0
		t=0
		while i < (len(lst)):
			while aux < len(linhanome):
				if(lst[i] in linhanome[aux]):
					auxvalor.append(linhavalor[aux])
					aux += 1
					i += 1
					if(aux == len(linhanome)):
						if(i < len(lst)):
							t = i
							while t <= len(lst):
								auxvalor.append(0.0)
								t+=1
							i = len(lst)+1
							aux = len(lst)+1
							
				elif(lst[i] not in linhanome[aux]):
					auxvalor.append(0.0)
					i+=1
					if(aux == len(linhanome)):
						if(i < len(lst)):
							t = i
							while t <= len(lst):
								auxvalor.append(0.0)
								t+=1
							i = len(lst)+1
							aux = len(lst)+1
		matvalor.append(auxvalor)
		linhaOri = arqOri.readline()
	#fim while
	#~ salvaMat(matvalor,"lucas.txt")
	return matvalor
#fim matrizEV

def matrizCos2(mat):
	mataux = matrizCos(mat)
	return mataux

def salvaMat(mat,nome):
	arquivo = open(nome,"a")
	for elem in mat:
		for pal in elem:
			arquivo.write(str(pal) + " ")
		arquivo.write("\n")
	arquivo.close() 
#fim salvaEV

def carregaMatConfu(nome):
	mat=[]
	lst = []
	strbuffer = ""
	arquivo = open(nome,"r")
	linha = arquivo.readline()
	while linha != "":
		for elem in linha:
			if(elem.isalnum() or elem == "."):
				strbuffer = strbuffer + elem
			if(elem == " "):	
				lst.append(strbuffer)
				strbuffer = ""
		linha = arquivo.readline()
		mat.append(lst)
		lst = []
	return mat
#fim carregaEV

def matrizTransposta(mat):
	aux=[]
	for j in range(len(mat[0])):
		linha=[]
		for i in range(len(mat)):
			linha.append(mat[i][j])
		aux.append(linha)
	
	return aux
	
	
def mostra_matriz(matriz):
	print('Matriz')
	for i in range(len(matriz)):
		
		for j in range(len(matriz[0])):
			print("|",end=" ")
			print (matriz[i][j], end =" ")
		print("|")
#fim mostra_matriz

def fazInsercao(lst):
	chave = 0
	for i in range(1, len(lst)):
		chave = lst[i]
		j = i - 1
		while j >= 0 and lst[j] > chave:
			lst[j + 1] = lst[j]
			j -= 1
		lst[j + 1] = chave
	return lst

def compoeEV2(endereco):
	#~ matnome=[]
	#~ matvalor=[]
	#~ linhanome=[]
	#~ linhavalor=[]
	#~ arqOri = open(endereco + "/bdev.txt","r")
	#~ linhaOri = arqOri.readline()
	#~ while linhaOri != "": 
		#~ #print(linhaOri[:-1])
		#~ nomeArq = open(endereco+"/"+linhaOri[:-1],"r")
		#~ linhaArq = nomeArq.readline()
		#~ linhanome=[]
		#~ linhavalor=[]
		#~ while linhaArq != "":
			#~ #print(linhaArq[:-1])
			#~ (nome,valor) = linhaArq.split(",")
			#~ linhanome.append(nome)
			#~ linhavalor.append(int(valor))
			#~ linhaArq = nomeArq.readline()
		#~ matnome = matnome + [linhanome] 
		#~ matvalor = matvalor + [linhavalor]
		#~ linhaOri = arqOri.readline()
	print(linhanome)
def matrizEV2(endereco):
	#~ lst = compoeEV(endereco)
	#~ matvalor = []
	#~ linhavalor = []
	#~ linhanome = []
	#~ i = 0
	#~ aux=0
	
	#~ arqOri = open(endereco + "/bdev.txt","r")
	#~ linhaOri = arqOri.readline()
	
	#~ while linhaOri != "": 
		#~ nomeArq = open(endereco+"/"+linhaOri[:-1],"r")
		#~ linhaArq = nomeArq.readline()
		#~ print(linhavalor)
		#~ linhavalor = []
		#~ linhanome=[]
		#~ aux=0
		
		#~ while linhaArq != "":
			#~ (nome,valor) = linhaArq.split(",")
			#~ while i <= len(lst):
				#~ if(lst[aux] not in nome):
					#~ linhavalor.append(0.0)
					#~ aux += 1
					#~ i = len(lst) + 2
					
				#~ if(lst[aux] in nome):
					#~ linhavalor.append(float(valor))
					#~ aux += 1
					#~ i = len(lst) + 2
					
			#~ #fim while 
			#~ i = 0
			#~ linhaArq = nomeArq.readline()
			#~ if(linhaArq == ""):
				#~ while len(linhavalor) < 10:
					#~ linhavalor.append(0.0)
		#~ #fim while
		#~ matvalor.append(linhavalor)
		#~ linhaOri = arqOri.readline()
	#~ #fim while
	
	#~ print(lst)
	return matvalor

	
def main():
	lstv = [1,2,3,1,2,1,4,6]
	#~ lstu = [5,6,1]
	#~ lstm = [[1,2,3]	,[5,6,1],[7,3,0],[8,1,2],[2,6,1],[2,1,5]]
	#~ lstx = matrizCos(lstm)
	#~ mostra_matriz(lstx)
	#~ print(cosseno(lstv,lstu))
	#~ print(compoeEV("//home/lucas/Documentos/codigos/trab prog2 jan/prog2-ativ-jan/vetnotebooks"))
	#~ salvaEV(compoeEV("//home/lucas/Documentos/codigos/trab prog2 jan/prog2-ativ-jan/vetnotebooks"))
	#~ mostra_matriz(matrizTransposta(matrizEV("//home/lucas/Documentos/codigos/trab prog2 jan/prog2-ativ-jan/vetnotebooks")))
	#~ mostra_matriz(matrizEV("//home/lucas/Documentos/codigos/trab prog2 jan/prog2-ativ-jan/vetnotebooks"))
	#~ mat = matrizEV("//home/lucas/Documentos/codigos/trab prog2 jan/prog2-ativ-jan/vetnotebooks")
	#~ mostra_matriz(matrizCos2(mat))
	#~ mostra_matriz((carregaMatConfu("lucas.txt")))
	#~ fazSelecao(lstv)
	#~ print(lstv)
	#~ lst = compoeEV("//home/lucas/Documentos/codigos/trab prog2 jan/prog2-ativ-jan/vetnotebooks")
	#~ print(fazInsercao(lst))
	mostra_matriz((matrizEV("//home/lucas/Documentos/codigos/trab prog2 jan/prog2-ativ-jan/vetnotebooks")))
	return 0

if __name__ == '__main__':
	main()
