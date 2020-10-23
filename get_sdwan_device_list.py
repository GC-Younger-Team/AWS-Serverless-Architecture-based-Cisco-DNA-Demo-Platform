import socket
import json
from get_device import get_device

def Logstash(event, context):
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    get_device_list=get_device(event, context)
   
    s.connect(('10.11.2.7', 6001))
    s.send(str(json.dumps(get_device_list)).encode('utf-8'))
    s.close()
   