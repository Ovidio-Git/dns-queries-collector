from requests import post
from os import getenv
from json import dumps
from logs.manager import logger 

# Ejecuta el comando 'ls' y captura la salida


collector_id = getenv('LUMU_COLLECTOR_ID')
lumu_client_key = getenv('LUMU_CLIENT_KEY')
#URL_TARGET = f"http://example.com/collectors/{collector_id}/dns/queries?key={lumu_client_key}"
URL_TARGET = ''

def send_to_api(payload: dict) -> bool:
    """ Send the payload to the Lumu API and return True if the action was successful
        Args:
            payload (dict): The payload to send to the Lumu API
        Returns:
            bool: True if the action was successful, False otherwise"""
    headers = {'Content-Type': 'application/json'}
    try:
        response = post(URL_TARGET, headers=headers, data=dumps(payload))
        if response.status_code == 200:
            logger.info("Data send to Lumu API successfully")
            print("Data send to Lumu API successfully")
        else:
            logger.error(f"Status code: {response.status_code}, Response: {response.text}")
        return True
    except Exception as e:
        logger.error(f"Exception: {e}")
        return False
        
def parse_log_file(chunk_raw) -> list[dict]:
    """ Process the log file with a hunk size of 500
        Args:
            file_path (str): The path of the file to process
        Returns:
            list[dict]: The processed data in a list of dictionaries"""
    chunk_cooked = []
    for line_bytes in chunk_raw[:10]:
        # Convert the line to a string and split it by spaces
        line_string = line_bytes.decode('utf-8')
        data = line_string.split(" ")
        print(data)
        # Append the processed data to the chunk_cooked list
        chunk_cooked.append({
            "timestamp": data[0] + "T" + data[1],
            "name": data[9],
            "client_ip": data[6],
            "client_name": None,
            "type": data[11]
        })
    print(chunk_cooked)
    return chunk_cooked
 
def send_to_lumu(file_stream):
    """ Process the log file with a chunk size of 500 and send it to the Lumu API
    
        Args:
            file_stream (file): The file to process"""
            
    # Define the chunk size
    chunk_size = 500
    # Read the file lines
    lines = file_stream.readlines()
    total_lines = len(lines)

    # Process the file in chunks
    for i in range(0, total_lines, chunk_size):
        # Get the chunk of lines to process 
        chunk = lines[i:i+chunk_size]
        chunk_payload = parse_log_file(chunk)
        send_to_api(chunk_payload)

    return total_lines