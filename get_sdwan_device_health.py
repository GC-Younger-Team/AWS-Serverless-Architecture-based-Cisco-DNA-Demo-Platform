import socket
import json
import pprint
from get_device_hardwarehealth import get_device_hardwarehealth

def Logstash(event, context):
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    device_hardwarehealth=get_device_hardwarehealth(event,context)
    
    s.connect(('10.11.2.7', 6002))
    s.send(str(json.dumps(device_hardwarehealth)).encode('utf-8'))
    s.close()

