import requests
import socket
import json
from requests.auth import HTTPBasicAuth
from get_token import get_token

def tcp_socket(event, context):
    def get_client_health():
        requests.packages.urllib3.disable_warnings()
        url = "https://10.10.1.2/dna/intent/api/v1/client-health"
        hdr = {'x-auth-token': get_token(event, context), 'content-type': 'application/json'}
        resp = requests.get(url, headers=hdr, verify=False)
        client_health = resp.json()
        return client_health
        
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('10.11.2.7', 7004))
        s.send(str(json.dumps(get_client_health())).encode('utf-8'))
        s.close()