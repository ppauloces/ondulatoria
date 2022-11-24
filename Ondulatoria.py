import numpy as np
import matplotlib.pyplot as plt
from math import pi
from numpy import arange
import matplotlib.pyplot
import math

# valores iniciais 
velocidade = float(input("[1] Insira uma velocidade em (m/s)metros por segundo: "))
frequencia = input("[2] Insira uma frenquência em (hz): ")

#calcula o comprimento de onda
comprimento = velocidade/float(frequencia)
# define o tamanho da amplitude
amplitude = float(input("[3] Insira uma amplitude em (m) metros: "))
# quantidade de ciclos
qtdCiclos = float(input("[4] Defina a quantidade de ciclos: "))
notacao=1
cont=0
newf= ""
# determina o tipo de frequencia
for i in frequencia:
    if i!=".":
        newf+=i
    if i==".":
        break
for i in newf:
    if cont!=0:
        notacao+=1
    cont+=1
    
if notacao-2<=8 and notacao-2>=0:
    print("=====================================")
    print("Esta é uma onda de rádio!")
if notacao-2>=9 and notacao-2<=11:
    print("=====================================")
    print("Esta é uma micro onda!")
if notacao-2>=12 and notacao-2<=14:
    print("=====================================")
    print("Este é um infra-vermelho!")
if notacao-2>=15 and notacao-2<=17:
    print("=====================================")
    print("Este é um ultra-violeta!")
if notacao-2>=18 and notacao-2<=20:
    print("=====================================")
    print("Este é um raio X !")
if notacao-2>=21 and notacao-2<=25:
    print("=====================================")
    print("Este é um raio gama !")

#Calcula índice de refração da luz no vácuo
c = 299792458
IndiceDeRefracao = (c/velocidade)
print("=====================================")
print("Indice de Refração :" ,IndiceDeRefracao)
#Calcula o comprimento de onda
print("=====================================")
print("Comprimento de onda:",comprimento," m")

eixoX = np.arange(0, comprimento*qtdCiclos, comprimento/1000)
eixoXduplicada = (eixoX * (pi*2))

eixoY = np.sin(eixoXduplicada/comprimento) * amplitude

plt.plot(eixoX, eixoY)

plt.grid(True)

def renderizarGrafico(xLabel, yLabel):
	matplotlib.pyplot.xlabel(xLabel)
	matplotlib.pyplot.ylabel(yLabel)
	matplotlib.pyplot.show()

renderizarGrafico("Comprimento de onda(m)","Amplitude(m)")

plt.show()

