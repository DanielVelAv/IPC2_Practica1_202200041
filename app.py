from flask import jsonify, Flask, request
from flask_cors import CORS
import Pila
import graphviz

app = Flask(__name__)
CORS(app)

miPila = Pila.Pila()

@app.route('/addPila', methods=['POST'])     
def addPila():
    if request.method == 'POST':
        valorLeido = request.form['valor']
        miPila.insertar(valorLeido)
        return jsonify({"msg": "ok"})
    
#Generar endpoint para crear el grafo de la pila    

@app.route('/graficarPila')
def graficarPila():

    valor = miPila.tope

    g = graphviz.Digraph()
    g.format = "jpg"



    grafo = ""
    grafo += '<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">'
    grafo += '<TR>'
    for i in range(valor):
    grafo += '''<</TABLE>>'''

    g.node('tabla', shape = 'plaintext', label = grafo )
    g.render()



@app.route('/getPila')  
def getPila():
    return jsonify({"pila": miPila.printPila()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)