import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from helpers import get_dominant_colors

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        # check if the post request has the file part
        k = int(request.form.get('amount_of_colors'))
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file.read()  # Read the file contents

            colors = get_dominant_colors(file, k)
            print(colors)

            colors_code = list()
            for color in colors:
                hex_value = '#{:02x}{:02x}{:02x}'.format(*color)
                colors_code.append(hex_value)
            print(colors_code)
           
            return render_template("colors.html", colors=colors_code)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)