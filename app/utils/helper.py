from requests import post
from os import getenv
from json import dumps
from logs.manager import logger 

collector_id = getenv('LUMU_COLLECTOR_ID')
lumu_client_key = getenv('LUMU_CLIENT_KEY')
URL_TARGET = f"http://example.com/collectors/{collector_id}/dns/queries?key={lumu_client_key}"
    
def send_to_api(payload: dict) -> bool:

    headers = {'Content-Type': 'application/json'}
    try:
        response = post(URL_TARGET, headers=headers, data=dumps(payload))
        if response.status_code == 200:
            logger.info("Data send to Lumu API successfully")
        else:
            logger.error(f"Status code: {response.status_code}, Response: {response.text}")
        return True
    except Exception as e:
        logger.error(f"Exception: {e}")
        return False



def parse_log_file(file_path):
    """ Process the log file with a hunk size of 500

        Args:
            file_path (str): The path of the file to process"""
    return True  # Devuelve si la acción fue exitosa

def send_to_lumu_api(file_stream):
    """ Process the log file with a chunk size of 500 and send it to the Lumu API
    
        Args:
            file_stream (file): The file to process"""
            
    # Define the chunk size
    chunk_size = 500
    # Read the file lines
    lines = file_stream.readlines()
    # Process the file in chunks
    for i in range(0, len(lines), chunk_size):
        # Get the chunk of lines to process 
        chunk = lines[i:i+chunk_size]
        print(f"Procesando bloque de {len(chunk)} líneas")  

    return len(lines)  


    # format: [ { "timestamp": "2021-01-06T14:37:02.228Z", "name": "www.example.com", "client_ip": "192.168.0.103", "client_name": "MACHINE-0987", "type": "A" } ]
    # enpoint: POST /collectors/{collector-id}/dns/queries?key={lumu-client-key}
    pass