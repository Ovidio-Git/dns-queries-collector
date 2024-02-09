from flask import Flask, request, render_template, redirect, url_for, flash
from os import getenv
from requests import post

app = Flask(__name__)
app.secret_key = getenv('FLASK_SECRET_LUMU')

# Define main path
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # test if the request hava files
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file:
            # seccion for process the file
            return redirect(url_for('result'))
    return render_template('index.html')



# Define result path with statics
@app.route('/result')
def result_upload():
    return 'test'

if __name__ == '__main__':
    app.run(debug=True)
