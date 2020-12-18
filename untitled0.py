# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qkoJfgjpph0XzfgTLQ22-vj-pLpDz2dF

## **Exercício 1**
"""

def multiplos():
  """função que diz quantos números pares, 
  múltiplos de 49 e 37 no intervalo de 1 a 5 milhões"""
  intervalo = 1
  contador = 0
  while (intervalo < 5000001):
    if (intervalo%2 == 0) and (intervalo%49 == 0) and (intervalo%37 == 0):
      contador = contador + 1
    intervalo = intervalo + 1
  return contador

multiplos()

"""## **Exercício 2**"""

import math

def posição_maior_elemento():
  """função que cria um vetor x com 10 posições
  e retorna a posição do maior elemento desse vetor"""

  vetor = [None]*10   #criei uma lista de valores vazios
  somatória = 0       #guarda a somatoria do vetor

  for i in range(10):
    if i%2 == 0:
      vetor[i] = 3**i + 7*(math.factorial(i))     #se o resto for igual a 0 (par) ele faz essa operacao. Caso contrario, faz a outra operacao
      somatória = somatória + vetor[i]

    else:
      vetor[i] = 2**i + 4*(math.log(i))
      somatória = somatória + vetor[i]

  posicao = vetor.index(max(vetor))
  média = somatória/10

  print("A posição do maior elemento é: ", posicao, "\nA média dos elementos contidos no vetor é: %10.2f" % média) 

posição_maior_elemento()

"""## **Exercício 3**"""

def notas(nota1, nota2, nota3, nota4, nota5):
  """função que lê a nota dos alunos e retorna
  o aluno com a maior nota e sua respectiva nota"""

  caderno_de_notas = {"Aluno 1": nota1, "Aluno 2": nota2, "Aluno 3": nota3,"Aluno 4": nota4,"Aluno 5": nota5}
  notas = list(dict.values(caderno_de_notas))
  nomes = list(dict.keys(caderno_de_notas))
  maior_nota = max(notas)                                                 #criado o dicionario, criei listas de nomes e de notas
                                                                          #peguei o max das notas junto com seu index
  if (notas.count(maior_nota) == 1):                                      #se caso tiverem mais de um aluno com a nota maxima
    index_maior_nota = notas.index(maior_nota)                            #o algoritmo avisa
    print("O aluno com a maior nota eh: ", nomes[index_maior_nota], "\nA nota dele foi: ", maior_nota)

  else:
    print("Mais de um aluno tirou a maior nota, a qual foi: ", maior_nota)


#notas(1,2,5,4,5)