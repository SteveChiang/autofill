#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import random
import json
import time
import socks
import socket
from random import randint

def getName():
	data = json.loads(open('name.json').read())
	firstNames = data['firstName']
	firstName = random.choice(firstNames)

	lastNames = data['lastName']
	lastName1 = random.choice(lastNames)
	lastName2 = random.choice(lastNames)

	result = firstName+lastName1+lastName2
	return result

def getPhone():
	numberHeader = '09'
	return numberHeader+str(random_with_N_digits(8))

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def getSelections():
	data = json.loads(open('selection.json').read())
	sel1 = random.choice(data['sel1'])
	sel2 = random.choice(data['sel2'])
	people = str(randint(1, 3))
	return [sel1, sel2, people]

def sendRequest():
	selection = getSelections()
	name = getName()
	phone = getPhone()

	# google server info
	url =  '' # POST url
	params = {
		'entry.': name, 
		'entry.': phone,
		'entry.': selection[0],
		'entry.': selection[1],
		'entry.': selection[2],
		'pageHistory': '0,1'
	}
	
	r = requests.post(url, data=params)
	print(name+"\t"+phone+"\n"+selection[0]+"\n"+selection[1]+"\n"+selection[2]+"\n========================")

def main():

	# tor proxy
	socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
	socket.socket = socks.socksocket
	while True:
		print("tor IP:"+requests.get("http://icanhazip.com").text)
		sendRequest()
		sleepIntevel = randint(1, 3)
		print("sleep for "+str(sleepIntevel)+" seconds\n")
		time.sleep(sleepIntevel)

if __name__ == "__main__":
    main()

