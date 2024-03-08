from flask import Flask, render_template, request
from database import db, posicoesXs, posicoesYs, posicoesZs, posicoesRs

passwords = db.table('passwords')
layouts = db.table('layouts')
users = db.table('users')

app = Flask('backend')
app = Flask(__name__.split('.')[0], static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/novo', methods=['POST'])
def Novo():
    coords = request.form['coords']
    return render_template("index.html", name=coords)

@app.route('/pegar_caminho', methods=['POST']) 
def Enviar():
    pass

@app.route(' /listas_caminhos', methods=['POST'])
def Selecao():
    return render_template("controle-robo.html")

@app.route('/atualizar', methods=['POST'])
def SelecaoDB():
    return render_template("controle-db.html")

@app.route('/deletar', methods=['POST'])
def SelecaoDB():
    return render_template("controle-db.html")