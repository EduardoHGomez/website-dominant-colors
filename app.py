from flask import Flask, flash, jsonify, redirect, render_template, request, session
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/images'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == "GET":
        return render_template('index.html')

    elif request.method == "POST":
        


        
        return render_template("layout.html", var=testing)
        

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)