# import win32com.client
# def sendEmail(message):
#     outlook = win32com.client.Dispatch('outlook.application')
#     mail = outlook.CreateItem(0)
#     mail.To = 'sahil20000720@gmail.com'
#     mail.Subject = 'TEST JERBS'
#     mail.Body = message
#     mail.Send()

import yagmail
import configparser

config = configparser.ConfigParser()
config.read('tele.config')


user = config['MAIL']['from']
app_password = config['MAIL']['key']
to = config['MAIL']['to'].split(',')


def sendEmail(content, subject):
    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject, content)
        print('Sent email successfully')
