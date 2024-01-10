from _logging import *
from time import sleep
import requests,sys
from threading import Thread
from _inputs import stdin
from pathlib import Path

version = '8.12.11'
port = 8080

if not sys.platform.startswith('linux'):
    pass
    log(f"Not a Linux system or supported distribution. You are on {Fore.GREEN}{sys.platform}{Fore.RESET}.", parent=parents.ERROR, time=False)
    #exit(0)
else:
    s = f'{sys.platform.split("linux")[1]} bit'
    log(f"Running on a Linux system or supported distribution. You are on {Fore.GREEN}{s if (sys.platform.split('linux')[1] or not sys.platform.split(' ')[0].lower() == 'linux') else ''}{Fore.RESET}.", parent=parents.SIGNAL, time=False)

if open(f"{Path().parent}/.run",'r').readline().partition(' ')[0] == 'true':
    log(f"Unable to start. Already running an instance of Amika Pi.", parent=parents.INSTANCE, time=False)
    exit(0)

open(f"{Path().parent}/.run",'w').write("true")

log("Starting AmikaPi server...", parent=parents.AMIKAPI)
try:
    _connect_test = requests.get('https://google.com/connect', timeout=5)
except requests.exceptions.HTTPError or requests.exceptions.Timeout or requests.exceptions.ConnectionError: log("No internet. Unable to start the server..", parent=parents.ERROR); exit(0)
log(f"""  {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} ABOUT     {Fore.BLUE}AmikaPi/{version}{Fore.RESET} (built for Linux ARM, 64/32 bit) {Style.RESET_ALL}
  {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} LIBS      {Fore.YELLOW}unavailable {Fore.RESET}{Style.RESET_ALL}
  {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} CPU       {Fore.RED}statistics unavailable {Fore.RESET}{Style.RESET_ALL}
  {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} MEMORY    {Fore.RED}statistics unavailable {Fore.RESET}{Style.RESET_ALL}""", parent=parents.NOPARENT, time=False)

pause_other_logging = False

def threaded_terminal():
    global pause_other_logging
    while True:
        inl = stdin("")
        if inl == "config":
            log(f""" {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} ABOUT     {Fore.BLUE}AmikaPi/{version}{Fore.RESET} (built for Linux ARM, 64/32 bit) {Style.RESET_ALL}
  {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} LIBS      {Fore.YELLOW}unavailable {Fore.RESET}{Style.RESET_ALL}
  {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} CPU       {Fore.RED}statistics unavailable {Fore.RESET}{Style.RESET_ALL}
  {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} MEMORY    {Fore.RED}statistics unavailable {Fore.RESET}{Style.RESET_ALL}""", parent=parents.NOPARENT, time=False)
        elif inl == "port":
            log(f" {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} PORT      {Fore.BLUE}AmikaPi/{version}{Fore.RESET} (built for Linux ARM, 64/32 bit) : {Fore.WHITE}{Back.GREEN}{port}{Fore.RESET}{Back.RESET} {Style.RESET_ALL}", parent=parents.NOPARENT, time=False)
        elif inl == "reset":
            pause_other_logging = True
            n = stdin("Are you sure you would like to reset your Amika connection? [y/N] ", ctrl_c_exit=False)
            if n.lower() == "y":
                log("OK.",parent=parents.SIGNAL)
                sleep(2)
                log("Resetting connection to the server...",parent=parents.HTTP)
                sleep(2)
                log("Connection reset, connection OK.",parent=parents.HTTP)
            elif n.lower() == 'n' or n == "":
                log("OK.",parent=parents.SIGNAL)
            pause_other_logging = False

try:
    Thread(target=threaded_terminal).start()
except KeyboardInterrupt: print("Exiting...");exit(0)

sleep(10)
log("AmikaPi daemon is running...", parent=parents.AMIKAPI)
sleep(4)

from distribution.stable import main

try:
    while True:
        internet = True
        try:
            _connect_test = requests.get('https://google.com/connect', timeout=5)
        except requests.exceptions.HTTPError or requests.exceptions.Timeout or requests.exceptions.ConnectionError: log("No internet. Unable to continue.", parent=parents.ERROR); internet=False
        if not pause_other_logging and internet:
            log(f"Status: {Fore.GREEN}online{Fore.RESET}", parent=parents.AMIKAPI)
        sleep(10)
except KeyboardInterrupt:
    open(f"{Path().parent}/.run",'w').write("false")
    print("....")
    exit(0)