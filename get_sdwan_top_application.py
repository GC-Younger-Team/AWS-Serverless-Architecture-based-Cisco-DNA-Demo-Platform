import socket
import json
import pprint
from get_application import get_application

def Logstash(event, context):
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    application=get_application(event,context)
    s.connect(('10.11.2.7', 6003))
    s.send(str(json.dumps(application)).encode('utf-8'))
    s.close()

