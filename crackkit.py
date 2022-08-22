from selenium import webdriver
from os import path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from message import message
import time

options = webdriver.ChromeOptions()
options.add_experimental_option(
    "excludeSwitches", ["ignore-certificate-errors"])
options.add_argument('headless')
options.add_argument('window-size=0x0')

cur_dir = path.dirname(__file__)
Chrome_driver = cur_dir+'\\'+'chromedriver.exe'

driver = webdriver.Chrome(executable_path=Chrome_driver)


def crackkit(text):

    if text != None:
        msg = []
        lines = text.split('\n')

        company = lines[0].split("**")[1]
        if "crackitupdates" in text:
            url = lines[-3]
            driver.get(url)

            attributes = driver.find_elements(
                By.XPATH, "//div[contains(@class, 'card-body')]//p")

            line = driver.find_elements(
                By.XPATH, "//div[contains(@class, 'card-body')]//a[2]")
            apply = line[0].get_attribute("href")

            for i in attributes:
                msg.append(i.text)

            return message(Company=company, Location=msg[-1], Qualification=msg[-5], Experience=msg[-6], Batch=msg[-4], Salary=msg[-2], Apply=apply)
        else:
            url = lines[-1]
            return message(Company=company, Apply=url)


def fresh(text):
    msg = []

    lines = text.split('\n')
    for line in lines:
        msg.append(line.split(':', 1)[-1].replace(' ', ''))

    try:
        driver.get(msg[-2])
        links = driver.find_elements(By.XPATH, '//p//a')
        links.reverse()
        for link in links:
            if "fresherjobinfo" not in link.get_attribute("href"):
                msg[-2] = link.get_attribute("href")
                break
    except:
        print('except')
        pass

    return message(Company=msg[0], Location=msg[1], Qualification=msg[2], Experience=msg[3], Batch="2023", Salary=msg[4], Apply=msg[-2])
