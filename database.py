from tinydb import TinyDB, Query

db = TinyDB('db.json')
idCoords = db.table('idCoords')
posicoesXs = db.table('PosicaoX')
posicoesYs = db.table('PosicaoY')
posicoesZs = db.table('PosicaoZ')
posicoesRs = db.table('PosicaoR')

for item in db:
    print(item)

def insert_coord(id, x, y, z, r):
    idCoords.insert({'id': id})
    posicoesXs.insert({'x': x})
    posicoesYs.insert({'y': y})
    posicoesZs.insert({'z': z})
    posicoesRs.insert({'r': r})
    return print('Coordenadas inseridas com sucesso!')

