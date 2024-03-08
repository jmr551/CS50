from flask import Flask, render_template, request
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload_image():
    if 'imagen' in request.files:
        

if __name__ == "__main__":
    app.run(debug=True)
