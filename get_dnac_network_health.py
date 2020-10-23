import requests
import socket
import json
from get_network_health import get_network_health

def tcp_socket(event, content):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('10.11.2.7', 7002))
        s.send(str(json.dumps(get_network_health(event, content))).encode('utf-8'))
        s.close()