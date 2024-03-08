from flask import Flask, render_template, request
from database import db, coordenadas

app = Flask(__name__.split('.')[0], static_folder='static', template_folder='templates')



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/novo', methods=['POST'])
def Novo():
    idCoords = request.form.get('id')
    x = request.form.get('x')
    y = request.form.get('y')
    z = request.form.get('z')
    r = request.form.get('r')
    coordenadas.insert({'id': idCoords, 'x': x, 'y': y, 'z': z, 'r': r})
    return render_template("index.html", name=coordenadas)

@app.route('/pegar_caminho/<name>', methods=['GET']) 
def pegarCaminho(name):
    if name in coordenadas:
        x = db.search(coordenadas.x == x)
        y = db.search(coordenadas.y == y)
        z = db.search(coordenadas.z == z)
        r = db.search(coordenadas.r == r)
        return f"As coordenadas da rota são: {x}, {y}, {z}, {r}"
    else:
        return "Coordenadas não encontradas"

@app.route('/listas_caminhos', methods=['GET'])
def listasCaminhos():
    all_coords = coordenadas.all()
    return f"Coordenadas: {all_coords}"

@app.route('/atualizar', methods=['POST'])
def Atualizar():
    idCoords = request.form.get('idEdit')
    if idCoords in coordenadas:
        x = request.form.get('x')
        y = request.form.get('y')
        z = request.form.get('z')
        r = request.form.get('r')
        coordenadas.update_one({'id': idCoords}, {'$set': {'x': x, 'y': y, 'z': z, 'r': r}})
        return render_template("index.html", id=idCoords, x=x, y=y, z=z, r=r)
    else:
        return "Coordenadas não encontradas"

@app.route('/deletar', methods=['POST'])
def Delete():
    idCoords = request.form.get('id')
    if idCoords in coordenadas:
        coordenadas.remove({'idDelete': idCoords})
        return render_template("index.html")
    else:
        return "Coordenadas não encontradas"
