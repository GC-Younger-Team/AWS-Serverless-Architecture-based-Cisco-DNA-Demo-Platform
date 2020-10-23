import socket
import json
from get_ips import get_ips

def Logstash(event, context):
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    ips = get_ips(event, context)
    s.connect(('10.11.2.7', 6007))
    s.send(str(json.dumps(ips)).encode('utf-8'))
    s.close()

