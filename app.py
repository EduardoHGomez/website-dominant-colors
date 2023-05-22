from flask import Flask, flash, jsonify, redirect, render_template, request, session
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == "GET":
        return render_template('index.html')

    elif request.method == "POST":
        testing = request.form.get('input-testing')
        # Return a response or redirect to another page
        return render_template("layout.html", var=testing)
        

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)