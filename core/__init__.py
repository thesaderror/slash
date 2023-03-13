import os 
import pyfiglet
from time import strftime
class color:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    orange = '\033[38;5;214m'

    whitebg = '\033[7m'
    redbg = '\033[41m'
    greenbg = '\033[102m'
    yellowbg = '\033[43m'
    bluebg = '\033[44m'
    graybg = "\033[48:5m"
    blackbg = '\u001b[40m'

    gray = '\033[37m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    
    include = '\033[95m'


class symbol:
    log = f"[{color.green}{strftime('%X')}{color.reset}]"
    found = f"[{color.greenbg}FOUND{color.reset}]"

    social_found =f"[{color.whitebg}FOUND{color.reset}]"
    forum_found  =f"[{color.whitebg}FOUND{color.reset}]"
    paste_found  =f"[{color.redbg}PASTE{color.reset}]"
    github_found  =f"[{color.redbg}GITHUB{color.reset}]"
    leakcheck_found  =f"[{color.redbg}LEAK-CHECK{color.reset}]"
    help_found   =f"[{color.underline}{color.bold}{color.green}HELP{color.reset}]"

    error = f"[{color.red}ERROR{color.reset}]"
    info = f"[{color.blackbg}{color.gray}INFO{color.reset}]"
    slash = f"""{color.redbg}{color.bold}Slash{color.reset}"""

class banner:
    slash= f'{color.redbg}{color.bold}{pyfiglet.figlet_format(" SlashX ",font="slant")}{color.reset}'


def clear():
    os.system("clear || cls")

def highlight(text,selected):
    o = ""
    text = text.lower()
    selected = selected.lower()
    text = text.replace(selected,f"{color.bold}{color.orange}{selected}{color.reset}")
    return text

def info_highlight(text):
    return f"{color.blackbg}{color.gray}{text}{color.reset}"


def error_highlight(text):
    return f"{color.blackbg}{color.red}{text}{color.reset}"



class css:

    alert_main = '''
    display: block;
    padding: 20px;
    border-left: 5px solid;
    '''
    success = alert_main+''' 
    background-color: #D5F5E3;
    border-left-color: #2ECC71;
    color: #2ECC71;
    '''
    info = alert_main+'''
    background-color: #D6EAF8;
    border-left-color: #3498DB;
    color: #3498DB;
    '''


    warning = alert_main+'''
    background-color: #FCF3CF;
    border-left-color: #F1C40F;
    color: #F1C40F;
    '''

    error = alert_main+'''
    background-color: #F2D7D5;
    border-left-color: #C0392B;
    color: #C0392B;
    '''
