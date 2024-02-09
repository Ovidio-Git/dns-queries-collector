from flask import Flask, request, render_template
from os import getenv
from requests import post 
from utils.helper import send_to_lumu, read_logs

app = Flask(__name__)
app.secret_key = getenv('FLASK_SECRET_LUMU')
 
# Define main path
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')
  
# Define result path with statics
@app.route('/send', methods=['POST'])
def send_log():
    if request.method == 'POST':
        print("Files:", request.files)
        print("Form:", request.form)
        
        if 'file' not in request.files:
            print('No file part')
            return render_template('index.html')
        
        file = request.files['file']
        if file:
            total_lines = send_to_lumu(file)
            print('Total lines:', total_lines)
            total_records = 6000
            client_ips_rank = {
                '45.238.196.2': {'hits': 426, 'percentage': 7.10},
            }
            host_rank = {
                'TTRTX.local': {'hits': 305, 'percentage': 5.08},
            }
            return render_template('stats.html', total_records=total_records, client_ips_rank=client_ips_rank, host_rank=host_rank)
    else:
        return render_template('index.html')
 
@app.route('/logs')
def logs_app():
    inputs_logs = read_logs()
    return render_template('logs.html', inputs_logs=inputs_logs)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8043)
