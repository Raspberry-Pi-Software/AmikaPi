from _logging import *
from time import sleep
import requests,sys

version = '8.12.11'

if not sys.platform.startswith('linux'):
    log(f"Not a Linux system or supported distribution. You are on {Fore.GREEN}{sys.platform}{Fore.RESET}.", parent=parents.ERROR, time=False)
    exit(0)
else:
    s = f'{sys.platform.split("linux")[1]} bit'
    log(f"Running on a Linux system or supported distribution. You are on {Fore.GREEN}{s if sys.platform.split('linux')[1] or sys.platform.split(' ')[0].lower() == 'linux' else ''}{Fore.RESET}.", parent=parents.SIGNAL, time=False)

log("Starting AmikaPi server...", parent=parents.AMIKAPI)
try:
    _connect_test = requests.get('https://google.com/connect', timeout=5)
except requests.exceptions.HTTPError or requests.exceptions.Timeout: log("No internet. Unable to start the server..", parent=parents.ERROR); exit(0)
log(f""" {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} ABOUT     {Fore.BLUE}AmikaPi/{version}{Fore.RESET} (built for Linux ARM, 64/32 bit) {Style.RESET_ALL}
  {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} LIBS      {Fore.YELLOW}unavailable {Fore.RESET}{Style.RESET_ALL}
  {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} CPU       {Fore.RED}statistics unavailable {Fore.RESET}{Style.RESET_ALL}
  {Fore.GREEN}*{Fore.RESET}{Style.BRIGHT} MEMORY    {Fore.RED}statistics unavailable {Fore.RESET}{Style.RESET_ALL}""", parent=parents.NOPARENT, time=False)