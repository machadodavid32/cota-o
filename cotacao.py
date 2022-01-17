import requests

from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes['text'] = texto

#A primeira ação para se fazer uma interface grafica é criar a janela do programa

janela = Tk()
janela.title('Cotação') #titulo do programa
janela.geometry('400x400')


texto_orientacao = Label(janela, text="Clique no botão para ver as cotações das moedas") #Primeira informação
texto_orientacao.grid(column=0, row=0, padx=10, pady=10) #é onde encaixamos o texto ou botão, se em cima, em baixo, esquerda, direita.

botao = Button(janela, text="Buscar cotações", comman=pegar_cotacoes)
botao.grid(column=0, row=1)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2)

janela.mainloop() # para que a janela criada não feche
