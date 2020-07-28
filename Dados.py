import PySimpleGUI as sg
from random import randint

sg.theme('DarkAmber')

layout = [
    [sg.Text('SEJA BEM VINDO AO DADO VIRTUAL')],
    [sg.Text('CLIQUE ABAIXO PARA JOGAR O DADO')],
    [sg.Button('CLIQUE AQUI')]
]
tela = sg.Window('DADO VIRTUAL', layout)
while True:
    valor_dado = randint(1, 6)
    evento, values = tela.read()
    if evento == sg.WIN_CLOSED:
        break
    layout.append(sg.Text(sg.popup(f'O DADO CAIU COM VALOR  {str(valor_dado)}')))
tela.close()
