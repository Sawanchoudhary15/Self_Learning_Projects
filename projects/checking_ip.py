import pyinputplus as co
import re


def check_ip(ip):
    pattern = r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$'
    return bool(re.fullmatch(pattern, ip))


ip = co.inputStr("enter ip address here")

if check_ip(ip):
    print(f"{ip} is a valid ip address")

else:
    print("its not a correct ip address")