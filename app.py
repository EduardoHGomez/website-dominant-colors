from flask import Flask, flash, jsonify, redirect, render_template, request, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def HelloWorld():
    return "Hello world"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)