import random
import requests
from pyfiglet import Figlet

def getnamelist():
    text_file = open("names.txt", "r")
    lines = text_file.read()
    linessplit = lines.splitlines()
    return linessplit

def pickran(list):
    name = random.choice(list)
    return name

def reqname(recname): 
    response = requests.get(f'https://api.agify.io?name={recname}')
    return response.text

def printname(responseible): 
    print(f'the respons i got was {responseible}')

def axtion(num):
    list = getnamelist()
    while num > 0:
        random_name = pickran(list)
        respons_name = reqname(random_name)
        printname(respons_name)
        num = num - 1
    ui()
    

def ui():
    f = Figlet(font='slant')
    print(f.renderText('ButterMilk\nSoftware'))
    kip = str(input('do you want to check somw random names Y/N :'))
    if kip == 'Y':
        num = int(input("how many random names do you want me to check :"))
        axtion(num)
    else:
        exit()

ui()
