import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from numpy import arange
import matplotlib.pyplot
import time

def introducao():
    sg.theme('reddit')
    sg.set_options(font=('Arial 16'),text_color = 'black')

    text = [
        [sg.Text("Ondulatória")]
    ]

    msg =  [
        [sg.Text("Projeto idealizado pelos alunos da EI-32 do IFBA - Campus Eunápolis: ")],
        [sg.Text("Paulo Amaral, João Sobral, Ryan Lima, Lara Beatriz e Rhanna Rocha")],
        [sg.Text("Prof. de Física: Dr. Flávio")],
        ]
    button = [
        [sg.Button("Começar simulação")]
    ]

    layout = [
        [sg.Push(),sg.Column(text),sg.Push(),],
        [sg.Column(msg)],
        [sg.Push(),sg.Column(button),sg.Push()]
    ]

    window = sg.Window('Ondulatória', layout=layout,element_justification='c')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Começar simulação":
            ondulatoria()

def ondulatoria():

    sg.theme('reddit')
    sg.set_options(font=('Arial 16'),text_color = 'black')

    text = [
        [sg.Text("Ondulatória")]
    ]

    inputs =  [
        [sg.Text("Insira uma velocidade em (m/s) metros por segundo: ",),sg.Input(size =(5,1))],
        [sg.Text("Insira uma frenquência em (hz): "),sg.Input(size =(5,1))],
        [sg.Text("Insira uma amplitude em (m) metros: "),sg.Input(size =(5,1))],
        [sg.Text("Defina a quantidade de ciclos: "),sg.Input(size =(5,1))],
        [sg.Text("Tipo de onda: "),sg.Text("",key='raio')],
        [sg.Text("",key='comprimento')],
        [sg.Text("",key='refracao')]
        
        ]
    button = [
        [sg.Button("Simular")]
    ]

    layout = [
        [sg.Push(),sg.Column(text),sg.Push(),],
        [sg.Column(inputs)],
        [sg.Push(),sg.Column(button),sg.Push()]
    ]

    window = sg.Window('Ondulatória', layout=layout,element_justification='l')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        
        notacao=1
        cont=0
        newf= ""
        # valores iniciais 
        velocidade = float(values[0])
        frequencia = values[1]
        # define o tamanho da amplitude
        amplitude = float(values[2])
        # quantidade de ciclos
        qtdCiclos = int(values[3])
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
            window['raio'].update("onda de rádio")
        if notacao-2>=9 and notacao-2<=11:
            window['raio'].update("micro-onda")
        if notacao-2>=12 and notacao-2<=14:
            window['raio'].update("infra-vermelho")
        if notacao-2>=15 and notacao-2<=17:
            window['raio'].update("ultra-violeta")
        if notacao-2>=18 and notacao-2<=20:
            window['raio'].update("raio-X!")
        if notacao-2>=21 and notacao-2<=25:
            window['raio'].update("raio-gama")
        #Calcula índice de refração da luz no vácuo
        c = 299792458
        IndiceDeRefracao = (c/velocidade)
        
        comprimento = velocidade/float(frequencia)

        #calcula o indice de refração e exibe na tela
        window['refracao'].update(f"Indice de refração: {IndiceDeRefracao}")
        #Calcula o comprimento de onda e exibe na tela
        window['comprimento'].update(f"Comprimento de onda: {comprimento}")

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

introducao()