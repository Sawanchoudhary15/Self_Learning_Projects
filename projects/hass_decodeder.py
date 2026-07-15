import pyinputplus as co
import re
import json
from pathlib import Path as path

def hash_codered():
    folder = path(__file__).parent
    hash = co.inputStr("enter your hass code here: ")
    with open(folder/"rainbow_table.json","r") as f:
        data = json.load(f)
        if hash in data:
            print(f"hash enter : {hash}")

            if re.fullmatch(r"[a-fA-F0-9]{32}", hash):
                print("Hash type: MD5 🟢")                

            elif re.fullmatch(r"[a-fA-F0-9]{40}", hash):
                print("Hash type: SHA1 🟢")

            elif re.fullmatch(r"[a-fA-F0-9]{64}", hash):
                print("Hash type: SHA256 🟡")

            elif re.fullmatch(r"[a-fA-F0-9]{128}", hash):
                print("Hash type: SHA512 🔴")
                
            else:
                print("Unknown hash type ❌")

            print(f"password : {data[hash]}")                  

        else:
            print("Hash not in rainbow table — try a bigger wordlist!")

hash_codered()