from flask import Flask, request, render_template
from os import getenv
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
        # check if the post request has the file part 
        if 'file' not in request.files:
            print('No file part')
            return render_template('index.html')
        # get the file from the request
        file = request.files['file']
        if file:
            # send the file to the Lumu API and get the results stats
            total_records, client_ips_rank, host_rank = send_to_lumu(file)
            return render_template('stats.html', total_records=total_records, top_client_ips=client_ips_rank, top_hosts=host_rank)
    else:
        return render_template('index.html')
 
@app.route('/logs')
def logs_app():
    # Read the logs and send them to the template
    inputs_logs = read_logs()
    return render_template('logs.html', inputs_logs=inputs_logs)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8043)
