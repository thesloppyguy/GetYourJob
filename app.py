from tokenize import group
from telethon import TelegramClient
import configparser
import datetime

config = configparser.ConfigParser()
config.read('tele.config')

api_id = config['KEY']['api_id']
api_hash = config['KEY']['api_hash']
msg_id = []
msg_grup = 0
groups = []

for key in config['GROUPS']:
    groups.append(config['GROUPS'][key])

for key in config['ID']:
    msg_id.append(int(config['ID'][key]))


client = TelegramClient('session_name', api_id, api_hash)
client.start()


def new_link(url):

    return url


def msg_parse(text):
    if msg_grup == 0:
        pass
        # print(text)
    else:
        if "B.Tech" in text:
            lines = text.split('\n')
            url = lines[-2].replace('Apply now: ', '')
            url = new_link(url)
            print(url)


# index = msg_id[0]
# max_ind = index
# for message in client.iter_messages(groups[0], offset_id=index, reverse=True):
#     if int(message.id) > max_ind:
#         max_ind = int(message.id)
#     print(message.id)
#     msg_parse(message.text)
#     msg_id[0] = max_ind


for grp in groups:
    index = msg_id[msg_grup]
    max_ind = index

    for message in client.iter_messages(grp, offset_id=index, reverse=True):
        if int(message.id) > max_ind:
            max_ind = int(message.id)

        msg_parse(message.text)
        msg_id[msg_grup] = max_ind
    msg_grup += 1


# Storing newest message id
for i in range(msg_grup):
    config['ID'][str(i)] = str(msg_id[i])
    # with open('tele.config', 'w') as configfile:
    #     config.write(configfile)
