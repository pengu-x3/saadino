#pengu-x3

import curses, random, colorama, time, os, sys, threading, itertools ,colored
from random import randint
from colored import fore, back, style
from time import sleep
from colorama import Fore
class bcolors:
    pink = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    white = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
print(bcolors.green + "the password is : saadino")
original_pin = "saadinodki"  # or '1122'
count=0
while count < 3:
    secret_pin = input(bcolors.green + 'Enter the password : '+ bcolors.yellow)
    if secret_pin == original_pin:
        print(bcolors.green + 'you unlocked the password')
        break
    else:
        print(bcolors.red + 'wrong password')
        count += 1
import time  # so we can call time.sleep()
original_pin = "saadino"
count=0
while count < 3:
    secret_pin = input(bcolors.green + 'enter the password again :' + bcolors.yellow)
    if secret_pin == original_pin:
        print(bcolors.green + 'access granted')
        break
    else:
        print(bcolors.red + 'sorry the password is incorrect wait 10 seconds and try again')
        count += 1
        time.sleep(10)  # timeout for 10 seconds

print(bcolors.yellow + '''

_______   _______  _______  ______  _________ _        _______
( ____ \ (  ___  )(  ___  )(  __  \ \__   __/( (    /|(  ___  )
| (   \/ | (   ) || (   ) || (  \  )   ) (   |  \  ( || (   ) |
| (_____ | (___) || (___) || |   ) |   | |   |   \ | || |   | |
(____ _ )|  ___  ||  ___  || |   | |   | |   | (\ \) || |   | |
      ) || (   ) || (   ) || |   ) |   | |   | | \   || |   | |
/\____) || )   ( || )   ( || (__/  )___) (___| )  \  || (___) |
\_______)|/     \||/     \|(______/ \_______/|/    )_)(_______)

by anonymous_x9''')

a = input(bcolors.green + "instagram account :" + bcolors.yellow)
print(bcolors.green + "searching for instagram account : " + bcolors.yellow + a)
sleep(1)
print(bcolors.green + "instagram account founded!")
sleep(1)
def menu():
    print(bcolors.red + "[1]" + bcolors.green + "find the ip address")
    print(bcolors.red + "[2]" + bcolors.green + "informations of account")
    print(bcolors.red + "[3]" + bcolors.green + "track the location")
    print(bcolors.red + "[0]" + bcolors.green + "exit")
def option3():
    print("")
menu()
option = int(input(bcolors.cyan + "select the option :"))
while option != 0:
    if option == 1:
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]","[■■■■■■■■■□]", "[■■■■■■■■■]"]
        for i in range(len(animation)):
            time.sleep(0.5)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")
        done = False
#here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\r''searching for ipv4' + c)
                sys.stdout.flush()
                time.sleep(0.1)
                def generate_random_ip(): 
                    return '.'.join( 
                        str(randint(0, 255)) for _ in range(4) ) 
                random_ip = generate_random_ip() 
                sys.stdout.write('\r ipv4 is :' + random_ip)

        t = threading.Thread(target=animate)
        t.start()

#long process here
        time.sleep(10)
        done = True
    elif option == 2:
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]","[■■■■■■■■□□]","[■■■■■■■■■□]", "[■■■■■■■■■]"]
        for i in range(len(animation)):
            time.sleep(0.5)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n""informations Downloaded in file.txt ")

    elif option == 3:
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]","[■■■■■■■■■□]", "[■■■■■■■■■]"]
        for i in range(len(animation)):
            time.sleep(0.5)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n""location data Downloaded in output")
    else:
        print("option rejected")
    print()
    menu()
    option = int(input("select option :"))
print(bcolors.red + "abord hacking")
