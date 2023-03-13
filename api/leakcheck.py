import requests 
import json 
from core import *
from core.ResultsCollector import resultcollector
def check(value):
    res = json.loads(requests.get(f"https://leakcheck.net/api/public?key=49535f49545f5245414c4c595f4150495f4b4559&check={value}").text)
    if(res["success"]==True):
        out = f"{symbol.leakcheck_found} \n"
        n = res['found']
        data = res["sources"]
        out+=f"     Leaks : {color.bold}{res['found']}{color.reset} | Passwords : {color.bold}{res['passwords']}{color.reset}\n\n"
        for i in range(0,n):
            out+=f"     {color.reset}[{color.bold}{i+1}{color.reset}] Leak : {color.redbg}{data[i]['name']}{color.reset} \tLeak Date : {color.yellowbg}{data[i]['date']}{color.reset}\n"

        print(out)
        resultcollector.add_result("leakcheck", res)
