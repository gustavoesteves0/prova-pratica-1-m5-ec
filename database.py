from tinydb import TinyDB, Query

db = TinyDB('db.json')
coordenadas = db.table('coordenadas')
x = db.table('x')
y = db.table('y')
z = db.table('z')
r = db.table('r')

for item in coordenadas:
    print(item)

def insert_coord(id, x, y, z, r):
    coordenadas.insert({'id': id})
    x.insert({'x': x})
    y.insert({'y': y})
    z.insert({'z': z})
    r.insert({'r': r})
    return print('Coordenadas inseridas com sucesso!')
