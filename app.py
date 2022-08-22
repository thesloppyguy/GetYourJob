from telethon import TelegramClient
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from sendMail import sendEmail
from os import path
from crackkit import fresh, crackkit, driver
import os
import datetime

config = configparser.ConfigParser()
config.read('tele.config')

api_id = config['KEY']['api_id']
api_hash = config['KEY']['api_hash']
msg_id = []
msg_grup = 0
groups = []
msg_array = []
disp_array = []


for key in config['GROUPS']:
    groups.append(config['GROUPS'][key])

for key in config['ID']:
    msg_id.append(int(config['ID'][key]))


client = TelegramClient('session_name', api_id, api_hash)
client.start()


def msg_parse(text):
    if msg_grup == 0:
        disp_array.append(crackkit(text))
        pass
    else:
        if "B.Tech" or "Any Degree" in text:
            disp_array.append(fresh(text))


for grp in groups:
    index = msg_id[msg_grup]
    max_ind = index

    for message in client.iter_messages(grp, offset_id=index, reverse=True):
        if int(message.id) > max_ind:
            max_ind = int(message.id)

        msg_array.append(msg_parse(message.text))

        msg_id[msg_grup] = max_ind

    msg_grup += 1


send = ' UPDATE '+str(msg_id[0])+'\n\n'
for i in disp_array:
    if i != None:
        send += 'Company Name :' + i.Company+'\n'
        send += 'Location :' + i.Location+'\n'
        send += 'Qualification :' + i.Qualification+'\n'
        send += 'Experience :' + i.Experience+'\n'
        send += 'Batch :' + i.Batch+'\n'
        send += 'Salary :' + i.Salary+'\n'
        send += 'Apply :' + i.Apply+'\n'
        send += "================================================================\n"

sendEmail(send, "UPDATE"+str(msg_id[0]))

# Storing newest message id
for i in range(msg_grup):
    config['ID'][str(i)] = str(msg_id[i])
    print(config['ID'][str(i)])
    with open('tele.config', 'w') as configfile:
        config.write(configfile)

driver.close()
