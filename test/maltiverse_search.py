#!/usr/bin/python3

'''
Description:  Python script to query IPv4 , Domain, URL and Has functions through the use of Maltiverse's open IoC Search Engine.
Reference:  https://whatis.maltiverse.com
            https://github.com/maltiverse/python-maltiverse
Author:  Kris Rostkowski
'''

from maltiverse import Maltiverse
import keyring
import json

# test ip function to query hard IP and save results to a json file
def get_ip():

    secret = keyring.get_password("maltiverse", "username")
    api = Maltiverse(secret)
    result = api.ip_get("110.189.222.98")
    #print(json.dumps(result, indent=2, sort_keys=True))

    with open("ip.json", "w") as ip_results:
        json.dump(result, ip_results)

get_ip()
