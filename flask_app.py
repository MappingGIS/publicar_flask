from flask import Flask, request, url_for, redirect, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', nombre="Curso de MappingGIS")


@app.route('/primer_mapa', methods=['GET', 'POST'])
def primer_mapa():
    if request.method == 'POST':
        # hacer cosas cuando se envía el formulario
        # Si el usuario actua sobre el botón se redirige la página
        # la redirección puede ser a la misma ruta o a otro lugar
        return redirect(url_for('index'))

    # mostrar el formulario, no fue enviado
    #Mientras el usuario no hace nada, es decir si no pulsa el botón
    #se muestra la página con el formulario/botón
    start_coords = (40.965, -5.664)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    folium_map.save('templates/map.html')
    return render_template('mapa_web.html', nombre="Mapa de la ciudad de Salamanca")


if __name__ == '__main__':
    app.run(debug=True)
