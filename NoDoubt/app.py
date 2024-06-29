from flask import Flask, render_template, request, jsonify
import spoonacular as sp
import requests
from googletrans import Translator

app = Flask(__name__)

# Inicializar la API de Spoonacular con tu clave API
api = sp.API("cbcda93d25d74167bfe66338eb41d536")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recetas')
def recetas():
    return render_template('recetas.html')

@app.route('/Inspiracion')
def insipiracion():
    return render_template('Inspiracion.html')

@app.route('/modosDeUso')
def modosdeuso():
    return render_template('modosDeUso.html')

@app.route('/quienes_somos')
def quienessomos():
    return render_template('quienes_somos.html')

@app.route('/buscar_recetas', methods=['POST'])
def buscar_recetas():
    ingredientes_usuario = request.json['ingredientes'].split(",")
    recetas = buscar_recetas_con_ingredientes(ingredientes_usuario)
    return jsonify(recetas)

@app.route('/detalles_receta', methods=['POST'])
def detalles_receta():
    receta_id = request.json['id']
    detalles_receta = obtener_detalles_receta(receta_id)
    detalles_en_espanol = traducir_detalles_a_espanol(detalles_receta)
    return jsonify(detalles_en_espanol)

def buscar_recetas_con_ingredientes(ingredientes):
    query = " ".join(ingredientes)
    response = api.search_recipes_complex(query=query)
    data = response.json()
    if 'results' in data and data['results']:
        recetas = [{'titulo': resultado['title'], 'id': resultado['id']} for resultado in data['results']]
    else:
        recetas = [{'titulo': 'No hay recetas', 'id': None}]
    return recetas

def obtener_detalles_receta(id_receta):
    url = f"https://api.spoonacular.com/recipes/{id_receta}/information"
    params = {'apiKey': 'cbcda93d25d74167bfe66338eb41d536'}
    response = requests.get(url, params=params, timeout=10)
    data = response.json()
    detalles_receta = {
        'titulo': data['title'],
        'tiempo_preparacion': f"{data['readyInMinutes']} minutos",
        'porciones': data['servings'],
        'ingredientes': [ingrediente['original'] for ingrediente in data['extendedIngredients']],
        'instrucciones': [paso['step'] for paso in data['analyzedInstructions'][0]['steps']] if data['analyzedInstructions'] else []
    }
    return detalles_receta

def traducir_detalles_a_espanol(detalles_receta):
    translator = Translator()
    titulo = translator.translate(detalles_receta['titulo'], src='en', dest='es').text
    ingredientes = [translator.translate(ingrediente, src='en', dest='es').text for ingrediente in detalles_receta['ingredientes']]
    instrucciones = [translator.translate(instruccion, src='en', dest='es').text for instruccion in detalles_receta['instrucciones']]
    detalles_en_espanol = {
        'titulo': titulo,
        'tiempo_preparacion': detalles_receta['tiempo_preparacion'],
        'porciones': detalles_receta['porciones'],
        'ingredientes': ingredientes,
        'instrucciones': instrucciones
    }
    return detalles_en_espanol

if __name__ == '__main__':
    app.run(debug=True)
