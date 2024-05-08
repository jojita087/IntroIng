import spoonacular as sp
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

    # Obtener los pasos de la receta seleccionada
    pasos_receta = obtener_pasos_receta(receta_seleccionada['id'])

    # Traducir los pasos de la receta a español
    pasos_en_espanol = traducir_pasos_a_espanol(pasos_receta)

    # Mostrar los pasos de la receta al usuario
    print("\nPasos para hacer la receta:")
    for i, paso in enumerate(pasos_en_espanol, 1):
        print(f"{i}. {paso}")

def obtener_pasos_receta(id_receta):
    # Obtener los pasos de la receta con el ID proporcionado
    response = api.get_analyzed_recipe_instructions(id_receta)
    data = response.json()

    # Extraer y formatear los pasos de la receta
    pasos = []
    for instruccion in data[0]['steps']:
        pasos.append(instruccion['step'])
    return pasos

def traducir_pasos_a_espanol(pasos):
    # Traducir los pasos de la receta a español
    translator = Translator()
    pasos_en_espanol = [translator.translate(paso, src='en', dest='es').text for paso in pasos]
    return pasos_en_espanol

# Solicitar al usuario que ingrese los ingredientes separados por comas
ingredientes_usuario = input("Ingrese los ingredientes separados por comas: ").split(",")

# Llamar a la función para buscar recetas con los ingredientes proporcionados por el usuario
buscar_recetas_con_ingredientes(ingredientes_usuario)
