#Carpeta del proyecto:
* No Doubt:
+ Contiene los siguientes archivos del proyecto:
  - index-2.html: 
  - Inspiración.html:
  - modosDeUso.html:
  - quienes_somos.html:
  - recetas.html:
  - style.css2.0.css:
    



# Tut Github:

- Wiki Github [Proyecto Alejandro](https://github.com/alecacerestel/ProyectoPdi)

- Video para usar Github [Video](https://www.youtube.com/watch?v=Z6VM-Gp3OGw&list=PL-gX0xg7VLB-1O02yLPCBsPUZyV_c9Owg&ab_channel=Developeando)

- Simulador de Raspeberry pi [Wokwi](https://wokwi.com/pi-pico)

# tut gemini api:
- https://ai.google.dev/tutorials/python_quickstart

- https://github.com/google/generative-ai-docs/blob/main/site/en/tutorials/python_quickstart.ipynb

- https://ai.google.dev/tutorials/quickstart?hl=es-419

# HTML:
- Insertar imagenes desde la web: (full) URL in the src attribute:
<img src="url completo" alt="texto que describe lo que hay"> style="width:128px;height:128px;"> 

- Para mover la imagen de izq o derecha al texto:
FORMA=
<p><img src="smiley.gif" alt="Smiley face" style="float:right;width:42px;height:42px;">
The image will float to the right of the text.</p>

<p><img src="smiley.gif" alt="Smiley face" style="float:left;width:42px;height:42px;">
The image will float to the left of the text.</p>


- Insertar imagen desde la web como fondo: (full) URL in the src attribute:
  para que no se repita la imagen y abarque la pantalla completa:
  FORMA=
  <style>
body {
  background-image: url('URL COMPLETO');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: 100% 100%;
}
</style>

- para tener el titulo del cuadro se debe ocupar <label for="lname">Cualquier titulo:</label><br>
- para ingresar un cuadro que pida información al usuario se debe ocupar <input type="text" id="lname">
# Spoonacular
- Página [Spoonacular](https://spoonacular.com/food-api/console#Profile)
# Cómo ejecutar el código
Para ejecutar el código antes debemos instalar las siguientes bibliotecas
```
pip install spoonacular
pip install googletrans==4.0.0-rc1
```
