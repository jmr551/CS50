from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def upload_page():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def handle_upload():
    if 'image' in request.files:
        file = request.files['image']
        filename = secure_filename(file.filename)
        # Cambia aquí la ruta para incluir "static"
        filepath = os.path.join("static", "images", filename)
        # Asegúrate de que la carpeta "static/images" exista
        file.save(filepath)
        # Pasa la ruta relativa a la carpeta static para la redirección
        return redirect(url_for('edit_page', image_path=os.path.join("images", filename)))
    return 'Could not upload the image', 400

@app.route('/edit')
def edit_page():
    image_path = request.args.get('image_path')
    return render_template('edit.html', image_path=image_path)

@app.route('/process-image', methods=['POST'])
def process_image():
    # Asumiendo que tienes una imagen cargada previamente en el servidor como punto de partida.
    # De lo contrario, necesitarás ajustar este código para manejar la carga de la imagen.
    img = Image.open('ruta/a/tu/imagen/original.jpg')

    # Ajustar la imagen según los valores recibidos
    brightness = float(request.form['brightness']) / 100
    contrast = float(request.form['contrast']) / 100
    saturation = float(request.form['saturation']) / 100
    blur = float(request.form['blur'])

    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness)

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)

    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(saturation)

    if blur > 0:
        img = img.filter(ImageFilter.GaussianBlur(blur))

    # Guardar la imagen modificada en un objeto BytesIO
    img_io = io.BytesIO()
    img.save(img_io, 'JPEG', quality=85)
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True)
