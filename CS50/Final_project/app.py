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

if __name__ == "__main__":
    app.run(debug=True)
