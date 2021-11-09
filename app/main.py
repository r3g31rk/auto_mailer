#!/usr/bin/python3
# -*- coding: iso-8859-1 -*

######################################################
# mailingSelenium
######################################################


import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from random import randint, choice


#############################################################
# FUNCTIONS & TOOLS
#############################################################
def read_file(filepath: str) -> str:
    """
    Function taking a filepath as an argument an returning its content as a string
    :param filepath: path of the file to read
    :return: a string
    """
    with open(filepath, 'r') as f:
        return f.read()


def get_senders(filepath: str) -> dict:
    res = {}
    with open(filepath, 'r') as f:
        for line in f:
            dd = line.strip().split(';', 1)
            k, v = dd[0], dd[-1]
            res[k] = v
    return res


def get_receivers(filepath: str) -> list:
    res = []
    with open(filepath, 'r') as f:
        for line in f:
            res.append(line.strip())
    return res


def get_mails(folder: str) -> list:
    res = []
    # Change the directory
    os.chdir(folder)
    # iterate through all files
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            res.append((file[:-4], read_file(file)))
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


def browser_set_profile(pf, preferences: dict):
    """
    Function to ease configuraiton of the selenium borwser's preferences
    :param pf: a virgin selenium webrowser profile
    :param preferences: dict with  configuration keys and values
    :return: a configured selenium webrowser profile
    """
    for k, v in preferences.items():
        pf.set_preference(k, v)
    return pf


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
    profile_preferences = {"http.response.timeout": 10, "dom.max_script_run_time": 10, "permissions.default.image": 2,
                           "general.useragent.override": UserAgent().random}
    profile = browser_set_profile(webdriver.FirefoxProfile(), profile_preferences)
    my_options = Options()
    my_options.headless = True  # Switch this value to display/hide the browser
    driver = webdriver.Firefox(options=my_options, firefox_profile=profile)
    driver.get("https://account.protonmail.com/login")
    random_sleep_time(5)

    # Filling the fields
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys(username)
    random_sleep_time(2)
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys(secret)
    random_sleep_time(3)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    random_sleep_time(20)

    driver.find_element_by_tag_name('body').send_keys('n')
    random_sleep_time(2)
    driver.find_element_by_xpath("//input[@type='text' and @data-testid='composer:to']").send_keys(recipient)
    random_sleep_time(2)
    driver.find_element_by_xpath("//input[@type='text' and @data-testid='composer:subject']").send_keys(about)
    random_sleep_time(2)

    # did not found another way than "manually" going to the next MESSAGE field with the TAB key
    driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
    driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
    driver.find_element_by_tag_name('body').send_keys(text)
    random_sleep_time(5)

    # did not found another way than "manually" going to the next MESSAGE field with the TAB key
    driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.ENTER)
    random_sleep_time(20)

    # CLOSING
    driver.quit()
    return 0


#############################################################
# MAIN PROGRAM
#############################################################
if __name__ == '__main__':
    senders = get_senders('../inputs/from.txt')
    receivers = get_receivers('../inputs/to.txt')
    mails = get_mails('../inputs/emails')
    for receiver in receivers:
        login, password = choice(list(senders.items()))
        for mail in mails:
            subject, message = mail[0], mail[1]
            # send_protonmail(login, password, receiver, subject, message)
            print(f'#'* 42 + f'\nfrom:{login}\tto:{receiver}\tabout:{subject}\n{message}')
    #     os.remove('geckodriver.log')
    # TODO: proper logging and cleaning of useless logs
    # TODO: packager le tout pour utiliser from everywhere

# TODO: test it under windows OS
