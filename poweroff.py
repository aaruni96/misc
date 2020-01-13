#!/bin/python3

import json
import requests
import os
import time

apiURL="https://api.telegram.org/bot"
botID=""    #your secret bot ID here
offset=0
while (1):
	try:
		r=requests.get(apiURL+botID+"/getUpdates?offset="+str(offset))
	except requests.exceptions.RequestException as e:
		continue
	data=json.loads(r.content.decode('utf-8'))
	if (len(data['result']) > 0):
		updateID=data['result'][0]['update_id']
		userID=data['result'][0]['message']['from']['id']
		userCommand=data['result'][0]['message']['text']
		if(userID==):    #the user you want to listen from
			if(userCommand=='poweroff'):
				os.system('sudo /usr/sbin/poweroff -f')
		offset=updateID+1
