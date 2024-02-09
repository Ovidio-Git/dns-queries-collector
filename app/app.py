from flask import Flask, request, render_template, redirect, url_for, flash
from os import getenv
from requests import post 
from .utils.helper import send_to_lumu_api 

app = Flask(__name__)
app.secret_key = getenv('FLASK_SECRET_LUMU')

# Define main path
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file:
            total_lines = send_to_lumu_api(file)  # Procesa y obtiene el total de líneas
            flash(f'Archivo procesado con éxito. Total de líneas: {total_lines}')
            return redirect(url_for('result'))
    else:
        return render_template('index.html')



# Define result path with statics
@app.route('/result')
def result_upload():
    return 'test'

if __name__ == '__main__':
    app.run(debug=True)
