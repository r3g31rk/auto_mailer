#!/usr/bin/python3
# -*- coding: iso-8859-1 -*


import pathlib
import os
import sys
from random import choice


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS,
        # and places our data files in a folder relative to that temp
        # folder named as specified in the datas tuple in the spec file
        base_path = os.path.join(sys._MEIPASS, 'data')
    except Exception:
        # sys._MEIPASS is not defined, so use the original path
        base_path = ''

    return os.path.join(base_path, relative_path)


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
    messages = folder_path.glob('*.txt')
    # iterate through all files
    for message in messages:
        res.append((message.stem, read_file(message)))
    return res


if __name__ == '__main__':

    mails_path = pathlib.Path.cwd().joinpath('inputs','messages')
    receivers_path = pathlib.Path.cwd().joinpath('inputs','to.txt')
    senders_path = pathlib.Path.cwd().joinpath('inputs','from.txt')

    # Getting information from the inputs
    print('Getting information from the inputs')
    senders = get_senders(senders_path)
    receivers = get_receivers(receivers_path)
    mails = get_mails(mails_path)
    # Looping through each receiver provided to sent every mail provided
    print('Looping through each receiver provided to sent every mail provided')
    for receiver in receivers:
        login, password = choice(list(senders.items()))
        for mail in mails:
            subject, message = mail[0], mail[1]
            print('#' * 42 + f'\nMAIL SENT from:{login}\tto:{receiver}\tabout:{subject}\n{message}\n' + '#' * 42)

    print('shutting down')

