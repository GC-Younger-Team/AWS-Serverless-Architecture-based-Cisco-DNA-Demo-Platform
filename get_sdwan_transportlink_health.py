import socket
import json
import pprint
from get_Transport_Health import get_Transport_Health

def Logstash(event, context):
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    Transport_Health=get_Transport_Health(event,context)
    s.connect(('10.11.2.7', 6004))
    s.send(str(json.dumps(Transport_Health)).encode('utf-8'))
    s.close()

