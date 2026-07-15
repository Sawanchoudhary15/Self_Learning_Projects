import pyinputplus as co
import time
import json
import re
import logging
from pathlib import Path as path
import socket
def check_ip(ip):
    pattern = r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$'
    return bool(re.fullmatch(pattern, ip))

def port_scanner():
    folder = path(__file__).parent
    logging.basicConfig(
    filename=folder/"port_scanner.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s")
    common_ports = {
    21:  "FTP",
    22:  "SSH",
    23:  "Telnet",
    25:  "SMTP",
    53:  "DNS",
    80:  "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306:"MySQL",
    3389:"RDP",
    8080:"HTTP-Alt"}

    target = co.inputStr("enter the name or ip of the site you want to scan: ")
    start_port = co.inputInt("enter the starting port",min=1,max=65535)
    ending_port = co.inputInt("enter the ending port",min=start_port,max=65535)
    open_port = 0
    try:
        if check_ip(target):
            ip = target
        else:
            ip = socket.gethostbyname(target)

    except socket.gaierror:
        print("Invalid IP or Domain")
        return
    start = time.time()
    print(f"🎯 Target : {target}")
    print(f"Resolved IP : {ip}")
    print(f"📡 Scanning ports {start_port}-{ending_port}...")

    for port in range(start_port,ending_port+1):
        # Create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)    # wait max 1 second per port
     
        # Try to connect to a port
        result = s.connect_ex((ip, port))
        print(f"Scanning Port {port}...", end="\r", flush=True)
        if result == 0:
            open_port +=1
            if port in common_ports:
                print(f"[Open] Port : {port} - {common_ports[port]}")
                logging.info(f"[Open] Port : {port} - {common_ports[port]}")
            else:
                logging.info(f"[Open] Port : {port} - Unknown")
                print(f"[Open] Port : {port} - Unknown")

        else:
                logging.info(f"Port {port} CLOSED")
        s.close()
                       
     
    

    print("✅ Scan complete!")
    print(f"Open ports : {open_port}")
    print(f"Time taken: {time.time() - start:.2f} seconds")

port_scanner()