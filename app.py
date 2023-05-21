from flask import Flask, flash, jsonify, redirect, render_template, request, session
#from helpers import get_dominant_colors

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        # Get the amount of colors (k)
        k = request.form.get("amount-k")


        # Load up the image

        # Do algorithm

        # Return 

        return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)