import socket
import json
import pprint
from get_urlf import get_urlf

def Logstash(event, context):
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    urlf=get_urlf(event,context)
    s.connect(('10.11.2.7', 6006))
    s.send(str(json.dumps(urlf)).encode('utf-8'))
    s.close()
    

