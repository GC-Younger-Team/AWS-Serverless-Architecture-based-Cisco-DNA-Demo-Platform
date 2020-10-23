import requests
import socket
import json
from requests.auth import HTTPBasicAuth
from get_token import get_token
from get_site_id import get_site_id

def tcp_socket(event, context):
    n = 1
    
    for site in get_site_id(event, context):
        
        def get_site_device():
            requests.packages.urllib3.disable_warnings()
            url = "https://10.10.1.2/dna/intent/api/v1/membership/%s" % get_site_id(event, context)[n]
            hdr = {'x-auth-token': get_token(event, context), 'content-type': 'application/json'}
            resp = requests.get(url, headers=hdr, verify=False)
            site_device = resp.json()
            return site_device
            
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('10.11.2.7', 7003))
            s.send(str(json.dumps(get_site_device())).encode('utf-8'))
            s.close()
        n = n+1