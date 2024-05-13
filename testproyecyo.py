import spoonacular as sp
import requests
from googletrans import Translator

# Inicializar la API de Spoonacular con tu clave API
api = sp.API("cbcda93d25d74167bfe66338eb41d536")

def buscar_recetas_con_ingredientes(ingredientes):
    # Crear la consulta de búsqueda de recetas con los ingredientes proporcionados
    query = " ".join(ingredientes)
    
    # Realizar la búsqueda de recetas con la API de Spoonacular
    response = api.search_recipes_complex(query=query)
    data = response.json()

    # Mostrar las recetas disponibles al usuario
    print("Recetas disponibles con los ingredientes proporcionados:")
    for i, resultado in enumerate(data['results'], 1):
        print(f"{i}. {resultado['title']}")

    # Solicitar al usuario que seleccione una receta
    seleccion = int(input("Seleccione el número de la receta que desea ver en detalle: "))

    # Obtener la receta seleccionada
    receta_seleccionada = data['results'][seleccion - 1]  # Restamos 1 porque los índices comienzan en 0

    # Obtener detalles de la receta seleccionada
    detalles_receta = obtener_detalles_receta(receta_seleccionada['id'])

    # Traducir los detalles de la receta a español
    detalles_en_espanol = traducir_detalles_a_espanol(detalles_receta)

    # Mostrar los detalles de la receta al usuario
    print("\nDetalles de la receta seleccionada:")
    print(f"Título: {detalles_en_espanol['titulo']}")
    print(f"Tiempo de preparación: {detalles_en_espanol['tiempo_preparacion']}")
    print(f"Número de porciones: {detalles_en_espanol['porciones']}")
    print("Ingredientes:")
    for ingrediente in detalles_en_espanol['ingredientes']:
        print(f"- {ingrediente}")
    print("Instrucciones:")
    for i, instruccion in enumerate(detalles_en_espanol['instrucciones'], 1):
        print(f"{i}. {instruccion}")

def obtener_detalles_receta(id_receta):
    # Construir la URL para obtener detalles de la receta
    url = f"https://api.spoonacular.com/recipes/{id_receta}/information"
    # Parámetros de la solicitud
    params = {
        'apiKey': 'cbcda93d25d74167bfe66338eb41d536',
    }
    # Realizar la solicitud con manejo de tiempo de espera
    response = requests.get(url, params=params, timeout=10)  # Aumenta el tiempo de espera a 10 segundos
    data = response.json()

    # Extraer y formatear los detalles de la receta
    detalles_receta = {
        'titulo': data['title'],
        'tiempo_preparacion': f"{data['readyInMinutes']} minutos",
        'porciones': data['servings'],
        'ingredientes': [ingrediente['original'] for ingrediente in data['extendedIngredients']],
        'instrucciones': [paso['step'] for paso in data['analyzedInstructions'][0]['steps']] if data['analyzedInstructions'] else []
    }
    return detalles_receta

def traducir_detalles_a_espanol(detalles_receta):
    # Traducir los detalles de la receta a español
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

# Solicitar al usuario que ingrese los ingredientes separados por comas
ingredientes_usuario = input("Ingrese los ingredientes separados por comas: ").split(",")

# Llamar a la función para buscar recetas con los ingredientes proporcionados por el usuario
buscar_recetas_con_ingredientes(ingredientes_usuario)
