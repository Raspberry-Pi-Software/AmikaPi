from colorama import Fore, Style, Back, init
from datetime import datetime
from typing import Literal
from enum import Enum
init(autoreset=True)

class parents():
    AMIKAPI = f"{Back.CYAN}{Style.BRIGHT}{Fore.WHITE} amikapi   {Back.RESET}{Style.RESET_ALL} "
    SIGNAL = f"{Back.YELLOW}{Style.BRIGHT}{Fore.WHITE} signal    {Back.RESET}{Style.RESET_ALL} "
    ERROR = f"{Back.RED}{Style.BRIGHT}{Fore.WHITE} error     {Back.RESET}{Style.RESET_ALL} "
    HTTP = f"{Back.BLUE}{Style.BRIGHT}{Fore.WHITE} http      {Back.RESET}{Style.RESET_ALL} "
    INSTANCE = f"{Back.MAGENTA}{Style.BRIGHT}{Fore.WHITE} instance  {Back.RESET}{Style.RESET_ALL} "
    NOPARENT = ""

def log(message:str, parent=parents.AMIKAPI,time=True):
    print(f"{f'[{Style.DIM}{datetime.now()}{Style.RESET_ALL}] ' if time else ''}{parent}{message}")