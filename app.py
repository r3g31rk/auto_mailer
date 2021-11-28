#!/usr/bin/python3
# -*- coding: iso-8859-1 -*

######################################################
# mailingSelenium
######################################################

import pathlib
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from fake_useragent import UserAgent
from random import randint, choice


#############################################################
# FUNCTIONS & TOOLS
#############################################################
def get_senders(filepath: pathlib.Path) -> dict:
    res = {}
    with filepath.open(mode='r') as f:
        for line in f:
            dd = line.strip().split(';', 1)
            k, v = dd[0], dd[-1]
            res[k] = v
    return res


def get_receivers(filepath: pathlib.Path) -> list:
    res = []
    with filepath.open(mode='r') as f:
        for line in f:
            res.append(line.strip())
    return res


def read_file(filepath: pathlib.Path) -> str:
    """
    Function taking a filepath as an argument an returning its content as a string
    :param filepath: path of the file to read
    :return: a string
    """
    with filepath.open(mode='r') as f:
        return f.read()


def get_mails(folder_path: pathlib.Path) -> list:
    res = []
    # iterate through all files
    for m in folder_path.glob('*.txt'):
        res.append((m.stem, read_file(m)))
    return res


def random_sleep_time(n: int):
    """
    Function to sleep a random number of seconds close to the provided input +-[10%-50%]
    :param n: number of seconds you want to approximately wait
    :return: nothing, just waiting a bit inside the program
    """
    p = randint(1, 5) / 10.0
    n *= 100
    nap = randint(round(n * (1 - p)), round(n * (1 + p))) / 100.0
    sleep(nap)
    # print(f'I had a nap of {nap} seconds')


def driver_setup(driver_path: pathlib.Path, headless_mode: bool) -> webdriver:
    """
    Function to setup the driver of the selenium headless browser
    :param driver_path: the path to the geckodriver.exe file
    :param headless_mode: True (False) if you want to hide (see) what's going on
    :return: a selenium webdriver object
    """
    options = webdriver.FirefoxOptions()
    options.set_preference("http.response.timeout", 10)
    options.set_preference('dom.max_script_run_time', 10)
    options.set_preference('permissions.default.image', 2)
    options.set_preference('general.useragent.override', UserAgent().random)
    options.headless = headless_mode
    service = Service(driver_path.as_posix())
    return webdriver.Firefox(service=service, options=options)


def send_protonmail(username: str, secret: str, recipient: str, about: str, text: str) -> int:
    """
    Function using Selenium to send an email from a protonmail account.
    :param username: account login (without @protonmail.com)
    :param secret: account password
    :param recipient: the person who will received the mail
    :param about: the title of the mail you send
    :param text: the message of the mail you send
    :return: zero if everything is going fine
    """

    # Preparing the browser
    driver = driver_setup(pathlib.Path.cwd().joinpath('driver', 'geckodriver.exe'), False)

    # Connecting to the provided protonmail account
    driver.get("https://account.protonmail.com/login")
    random_sleep_time(5)

    # Filling the fields
    driver.find_element(By.ID, 'username').clear()
    driver.find_element(By.ID, 'username').send_keys(username)
    random_sleep_time(2)
    driver.find_element(By.ID, 'password').clear()
    driver.find_element(By.ID, 'password').send_keys(secret)
    random_sleep_time(3)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    random_sleep_time(20)
    driver.find_element(By.TAG_NAME, 'body').send_keys('n')
    random_sleep_time(2)
    driver.find_element(By.XPATH, "//input[@type='text' and @data-testid='composer:to']").send_keys(recipient)
    random_sleep_time(2)
    driver.find_element(By.XPATH, "//input[@type='text' and @data-testid='composer:subject']").send_keys(about)
    random_sleep_time(2)

    # did not found another way than "manually" going to the next MESSAGE field with the TAB key
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
    driver.find_element(By.TAG_NAME, 'body').send_keys(text)
    random_sleep_time(3)

    # did not found another way than "manually" going to the next SEND button (from the MESSAGE filed) with the TAB key
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.ENTER)
    random_sleep_time(5)

    # closing
    driver.quit()
    return 0


#############################################################
# MAIN PROGRAM
#############################################################
if __name__ == '__main__':
    # Getting information from the inputs
    print('Gathering inputs info')
    senders = get_senders(pathlib.Path.cwd().joinpath('inputs', 'from.txt'))
    receivers = get_receivers(pathlib.Path.cwd().joinpath('inputs', 'to.txt'))
    mails = get_mails(pathlib.Path.cwd().joinpath('inputs', 'messages'))
    print(f'---> {len(mails)} email(s) will be sent TO {len(receivers)} account(s) taking {len(mails) * len(receivers) * 1.2} minute(s)')
    # Looping through each receiver provided to sent every mail provided
    print('Looping through each receiver provided to sent every mail provided')
    for receiver in receivers:
        login, password = choice(list(senders.items()))
        for mail in mails:
            subject, message = mail[0], mail[1]
            send_protonmail(login, password, receiver, subject, message)
            print('#' * 42 + f'\nMAIL SENT from:{login}\tto:{receiver}\tabout:{subject}\n' + '#' * 42)

    # Cleaning
    pathlib.Path.cwd().joinpath('geckodriver.log').unlink()
    print('Cleaning and shutting down')

# TODO: cook the recipes for mailing with gmail which should be the most used**
