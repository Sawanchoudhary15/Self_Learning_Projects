import json
import re
from pathlib  import Path as path 


counting = {}
folder = path(__file__).parent

def check_ip(ip):
    pattern = r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$'
    return bool(re.fullmatch(pattern, ip))


with open(folder/"server.txt","r") as f:
    data = f.read()




ip = data.split()
for item in ip:
    if check_ip(item):
        counting[item] = counting.get(item, 0) + 1
    
for ip, count in counting.items():
    print(f"{ip}  →  {count} time")
        
