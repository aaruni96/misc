#!/usr/bin/python3

import json
import requests
import os
import time

apiURL="https://api.telegram.org/bot"
botID=""	#secret bot iD
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
		offset=updateID+1
		if(userID==):		#insert telegram user ID
			if(userCommand=='poweroff'):
				try:
					r=requests.get(apiURL+botID+"/getUpdates?offset="+str(offset))
				except requests.exceptions.RequestException as e:
					print(e)
				os.system('sudo /sbin/poweroff -f')
			else:
				try:
					r=requests.get(apiURL+botID+"/sendMessage?chat_id="+str(userID)+"&text="+userCommand)
				except requests.exceptions.RequestException as e:
					print(e)
