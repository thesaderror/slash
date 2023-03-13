from core import (
    banner,
    color,
    symbol,
    clear,
    highlight,
    info_highlight,
    error_highlight,
    css
)

from api.extract import *
from api.leakcheck import check as leak 
from api.leakcheck import check as leakcheck 
from core.ResultsCollector import resultcollector
import json
from core.scrape import *
import sys
import threading 
try:
    from urllib.request import urlopen
except:
    print(f"{color.redbg}Please use python version >3.0.{color.reset} {color.bold}Otherwise write issue by using {color.greenbg}official github{color.reset}{color.bold} repo to get better support.{color.reset}")
    sys.exit(0)

class config:
    socmint = "./.db/socmint.json"
    tmout = 4
    notapi_fn = "{} {} : {}"
    notapi_nf = "{} {} : {}"


class gathered:
    profiles = []

    locations = []
    names = []
    educations = []
    bios = []
    linked_urls = []
    user_infos = []
    phone_numbers = []
    mails = []


def parse(key,value,from_name,from_url):
    if(key=="Location"):
        #print(value)
        gathered.locations.append({"name":from_name,"source":from_url,"value":value})
        #print(gathered.locations)
    elif(key=="Name"):
        gathered.names.append({"name":from_name,"source":from_url,"value":value})
    elif(key=="Education"):
        gathered.educations.append({"name":from_name,"source":from_url,"value":value})
    elif(key=="Bio"):
        gathered.bios.append(value)
        threading.Thread(target=func_extract,args=(from_name,from_url,value)).start()

    elif(key=="Website"):
        gathered.linked_urls.append({"name":from_name,"source":from_url,"value":value})
    elif(key=="User Info"):
        gathered.user_info.append(value)
        gathered.user_infos.append({"name":from_name,"source":from_url,"value":value})

    #resultcollector.add_result(["parse1",f"profiles: {gathered.locations}, {gathered.names}, {gathered.educations}, {gathered.bios}, {gathered.linked_urls}, {gathered.user_infos}"])
    
    return gathered

def get_db():
    with open(config.socmint,"r") as f:
        return json.loads(f.read())

def func_extract(from_name,from_url,value):
    try:
        nums = extract.phone(from_name,value)
        if(len(nums)!=0):
            for i in nums:
                gathered.phone_numbers.append({"name":from_name,"source":from_url,"value":i})
                leakcheck(value)
    except Exception as e:
        print(e)

    try:
        mails = extract.mail(from_name,value)

        #print(mails)

        if(len(mails)!=0):
            for j in mails:
                gathered.mails.append({"name":from_name,"source":from_url,"value":j})
                leakcheck(value)
    except Exception as e:
        print(e)

def parse(key,value,from_name,from_url):
    result = {}
    if(key=="Location"):
        #print(value)
        gathered.locations.append({"name":from_name,"source":from_url,"value":value})
        #print(gathered.locations)
    elif(key=="Name"):
        gathered.names.append({"name":from_name,"source":from_url,"value":value})
    elif(key=="Education"):
        gathered.educations.append({"name":from_name,"source":from_url,"value":value})
    elif(key=="Bio"):
        gathered.bios.append(value)
        threading.Thread(target=func_extract,args=(from_name,from_url,value)).start()

    elif(key=="Website"):
        gathered.linked_urls.append({"name":from_name,"source":from_url,"value":value})
        leakcheck(value)
    elif(key=="User Info"):
        gathered.user_info.append(value)
        gathered.user_infos.append({"name":from_name,"source":from_url,"value":value})

    #resultcollector.add_result(["parse2",f"profiles: {gathered.locations}, {gathered.names}, {gathered.educations}, {gathered.bios}, {gathered.linked_urls}, {gathered.user_infos}"])
    return [gathered, result]
