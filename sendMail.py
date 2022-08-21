import win32com.client


def sendEmail(message):
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'sahil20000720@gmail.com'
    mail.Subject = 'TEST JERBS'
    mail.Body = message
    mail.Send()
