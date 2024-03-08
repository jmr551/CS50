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
        image = secure_filename(file.filename)
        filepath = os.path.join("imagen", filename)
        file.save(filepath)
        return redirect(url_for('edit_page', image_path=filepath))
    return 'Could not upload the image', 400

@app.route('/edit)

if __name__ == "__main__":
    app.run(debug=True)