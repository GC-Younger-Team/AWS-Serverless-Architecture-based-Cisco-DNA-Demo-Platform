import requests
import socket
import json
from requests.auth import HTTPBasicAuth
from get_token import get_token
from get_serial_no import get_serial_no

def tcp_socket(event, context):
    n = 0
    
    for device in get_serial_no(event, context):
        search_serial = {"serialNumber": "%s" % get_serial_no(event, context)[n]}
        n = n+1
        
        def get_device_serial():
            requests.packages.urllib3.disable_warnings()
            url = "https://10.10.1.2/api/v1/network-device"
            hdr = {'x-auth-token': get_token(event, context), 'content-type': 'application/json'}
            resp = requests.get(url, headers=hdr, params=search_serial, verify=False)
            device_serial = resp.json()
            return device_serial
            
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('10.11.2.7', 7001))
            s.send(str(json.dumps(get_device_serial())).encode('utf-8'))
            s.close()