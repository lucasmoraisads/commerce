from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page_home():
    return render_template("home.html")


@app.route('/produtos')
def page_produtos():

    itens = [
        {'id': 1, 'nome':'Celular', 'cod_barra':'91818374634782', 'preco': 1200},
        {'id': 2, 'nome':'Notebook', 'cod_barra':'29821782378931', 'preco': 3500},
        {'id': 3, 'nome':'Teclado', 'cod_barra':'340893128420012', 'preco': 120},
        {'id': 4, 'nome':'Monitor', 'cod_barra':'4389439323229323', 'preco': 800},
        {'id': 5, 'nome':'Mause', 'cod_barra':'579560967945696', 'preco': 100},
        {'id': 6, 'nome':'Gabinete', 'cod_barra':'609950349344958', 'preco' : 250},
        {'id': 7, 'nome':'Placa Mãe', 'cod_barra':'78983423920943', 'preco': 580},
        {'id': 8, 'nome':'SSD', 'cod_barra':'8459040598238984', 'preco':160},
    ]
    return render_template("produtos.html", itens=itens )




