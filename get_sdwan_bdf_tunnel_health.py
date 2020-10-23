import socket
import json
import pprint
from get_Tunnel_Health import get_Tunnel_Health

def Logstash(event, context):
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    Tunnel_Health=get_Tunnel_Health(event,context)
    s.connect(('10.11.2.7', 6005))
    s.send(str(json.dumps(Tunnel_Health)).encode('utf-8'))
    s.close()

