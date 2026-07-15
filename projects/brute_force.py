import pyinputplus as co
from pathlib import Path as path
import json
import time
import logging

def brute_Force():
    folder = path(__file__).parent
    with open(folder / "brute_force.txt") as f:
        data = [line.strip() for line in f]
    SECRET = "h4ck3r99"

    logging.basicConfig(
    filename=folder/"password_attempts.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s")

    
    for attempt,passwd in enumerate(data,start=1):
        if passwd ==  SECRET:
            print(f"the following {passwd} is the passwd\n total no of attempt took me to find? {attempt}")
            logging.info(f"[ATTEMPT {attempt}] Trying: {passwd} PASSWORD FOUND")
            time.sleep(.05)

            break


        elif passwd != SECRET:
            logging.info(f"[ATTEMPT {attempt}] Trying: {passwd} FAILED")
            time.sleep(.05)


        else:
            print("sorry we cant find your passwd with this file")

brute_Force()