from flask import Flask, json, request, jsonify

app = Flask(__name__)


# 1.
def funcion_1(diccionario, clave, valor):
    diccionario[clave] = valor
    return diccionario

# 2.
def funcion_2(diccionario, clave):
    if clave in diccionario:
        del diccionario[clave]
    return diccionario

# 3.
def funcion_3(diccionario, clave, nuevo_valor):
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        return True
    return False

# 4.
def funcion_4(dic1, dic2):
    return {**dic1, **dic2}

# 5.
def funcion_5(conjunto, elemento):
    if elemento not in conjunto:
        conjunto.add(elemento)
        return True
    return False

# 6.
def funcion_6(conjunto, elemento):
    if elemento in conjunto:
        conjunto.remove(elemento)
        return True
    return False

# 7. 
def funcion_7(conj1, conj2):
    return conj1.union(conj2)

# 8.
def funcion_8(conj1, conj2):
    return conj1.difference(conj2)

# 9.
def funcion_9(tupla, elemento):
    nueva_tupla = tupla + (elemento,)
    return nueva_tupla

# 10
def funcion_10(tupla, elemento):
    lista = list(tupla)
    if elemento in lista:
        lista.remove(elemento)
    return tuple(lista)

# 11
def funcion_11(tupla1, tupla2):
    return tupla1 + tupla2

# 12
def funcion_12(tupla):
    return tupla[::-1]

# 
@app.route('/')
@app.route('/wellcome/')
@app.route('/wellcome/<name>')
@app.route('/wellcome/<int:ncontrol>')
@app.route('/wellcome/<name>/<int:ncontrol>')
def bienvenido(name=None, ncontrol=None):
    if name is None and ncontrol is None:
        return 'Bienvenido '
    elif name is not None and ncontrol is None:
        return f'Bienvenido {name}'
    elif name is None and ncontrol is not None:
        return f'El número recibido es: {ncontrol}'
    else:
        return f'Bienvenido {name}, tu número de control es: {ncontrol}'

@app.route("/agregar/<path:diccio>/<clave>/<valor>", methods=['POST'])
def agregar(diccio, clave, valor):
    diccionario = json.loads(diccio)
    resultado = funcion_1(diccionario, clave, valor)
    return json.dumps(resultado)

@app.route("/eliminar/<path:diccio>/<clave>", methods=['DELETE'])
def eliminar(diccio, clave):
    diccionario = json.loads(diccio)
    resultado = funcion_2(diccionario, clave)
    return json.dumps(resultado)

@app.route("/modificar/<path:diccio>/<clave>/<nuevo_valor>", methods=['PUT'])
def modificar(diccio, clave, nuevo_valor):
    diccionario = json.loads(diccio)
    exito = funcion_3(diccionario, clave, nuevo_valor)
    return json.dumps({"exito": exito})

@app.route("/combinar_diccionarios/<path:diccio1>/<path:diccio2>", methods=['POST'])
def combinar(diccio1, diccio2):
    diccionario1 = json.loads(diccio1)
    diccionario2 = json.loads(diccio2)
    resultado = funcion_4(diccionario1, diccionario2)
    return json.dumps(resultado)

@app.route("/agregar_conjunto/<path:conjunto>/<elemento>", methods=['POST'])
def agregar_elemento(conjunto, elemento):
    conjunto = set(json.loads(conjunto))
    resultado = funcion_5(conjunto, elemento)
    return json.dumps({"exito": resultado, "conjunto": list(conjunto)})

@app.route("/eliminar_conjunto/<path:conjunto>/<elemento>", methods=['DELETE'])
def eliminar_elemento(conjunto, elemento):
    conjunto = set(json.loads(conjunto))
    resultado = funcion_6(conjunto, elemento)
    return json.dumps({"exito": resultado, "conjunto": list(conjunto)})

@app.route("/combinar_conjuntos/<path:conjunto1>/<path:conjunto2>", methods=['POST'])
def combinar_conjuntos_route(conjunto1, conjunto2):
    conjunto1 = set(json.loads(conjunto1))
    conjunto2 = set(json.loads(conjunto2))
    resultado = funcion_7(conjunto1, conjunto2)
    return json.dumps(list(resultado))

@app.route("/agregar_a_tupla/<path:tupla>/<elemento>", methods=['POST'])
def agregar_a_tupla_route(tupla, elemento):
    tupla = tuple(json.loads(tupla))
    nueva_tupla = funcion_9(tupla, elemento)
    return json.dumps(nueva_tupla)

@app.route("/eliminar_de_tupla/<path:tupla>/<elemento>", methods=['DELETE'])
def eliminar_de_tupla_route(tupla, elemento):
    tupla = tuple(json.loads(tupla))
    nueva_tupla = funcion_10(tupla, elemento)
    return json.dumps(nueva_tupla)

@app.route("/concatenar_tuplas/<path:tupla1>/<path:tupla2>", methods=['POST'])
def concatenar_tuplas_route(tupla1, tupla2):
    tupla1 = tuple(json.loads(tupla1))
    tupla2 = tuple(json.loads(tupla2))
    nueva_tupla = funcion_11(tupla1, tupla2)
    return json.dumps(nueva_tupla)

@app.route("/revertir_tupla/<path:tupla>", methods=['GET'])
def revertir_tupla_route(tupla):
    tupla = tuple(json.loads(tupla))
    nueva_tupla = funcion_12(tupla)
    return json.dumps(nueva_tupla)


if __name__ == "__main__":
    app.run(debug=True)

#   Test-. curl -X POST http://127.0.0.1:5000/agregar/%7B%22a%22%3A%201%7D/clave_nueva/valor_nuevo

# se realiza un POST a la ruta /agregar_conjunto con el conjunto {a: 1} y

#URL de Git por que solo deja subir archivos-. https://github.com/Trejillo-Joe/Pr-ctica-3-Flask---diccionarios-tuplas-y-conjuntos
