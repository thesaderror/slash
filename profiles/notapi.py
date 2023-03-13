from profiles.autoimport import *
from api.scrape import *
import threading
from core.ResultsCollector import resultcollector
def ozel_scrape(url,username):
    try:
        if(url.startswith("https://www.instagram.com/")):
            user = InstagramUser(username)
            email, phone_number = user.user_data['business_email'], user.user_data['business_phone_number']
            func_extract("instagram", url, f"{email} {phone_number}")
            #print(user.biography)
            parse("Bio",user.biography,"instagram",url)
            resultcollector.add_result(["instagram",user.biography])
    except:
        pass
    


def notapi(username,dct):
    url = (dct["url"]).format(username)
    desc = dct["desc"]
    name = dct["name"]
    nf = dct["messages"]["notfound"]
    scrape = dct["scrape"]
    method = dct["method"]

    htext = highlight(url,username)
    if(not scrape):
        if(type(nf)==int):
            r = urlopen(url,timeout=config.tmout)
            if(r.getcode()!=nf):
                print((config.notapi_fn).format(symbol.social_found,f"{color.red}{color.bold}social/{color.green}{color.bold}{name}{color.reset}",htext))
                threading.Thread(target=ozel_scrape,args=(url,username)).start()
                return {name:url}
            else:
                pass

        else:
            r = urlopen(url,timeout=config.tmout)

            try:source = r.read().decode("utf-8")
            except:source = r.read().decode("latin-1")

            if(not nf in source):
                print((config.notapi_fn).format(symbol.social_found,f"{color.red}{color.bold}social/{color.green}{color.bold}{name}{color.reset}",htext))
                threading.Thread(target=ozel_scrape,args=(url,username)).start()
                return {name:url}
            else:
                pass


    
    else: # Scrape
        
        _scrape = dct["_scrape"]
        lsc = len(_scrape)
        if(type(nf)==int): # 404 ? or other status_codes

            r = urlopen(url,timeout=config.tmout)

            try:source = r.read().decode("utf-8")
            except:source = r.read().decode("latin-1")
            
            if(r.getcode()!=nf):
                print((config.notapi_fn).format(symbol.social_found,f"{color.red}{color.bold}social/{color.green}{color.bold}{name}{color.reset}",htext))
                scraped = scrapefunc(_scrape,url,name,source)
                if(scraped != ""):
                    print()
                    print(scraped)
                threading.Thread(target=ozel_scrape,args=(url,username)).start()
                return {name:url}

        else:
            r = urlopen(url,timeout=config.tmout)
            try:
                source = r.read().decode("utf-8")
            except:
                source = r.read().decode("latin-1")

            if(not nf in source): # some text that not appears if there is a user
                print((config.notapi_fn).format(symbol.social_found,f"{color.red}{color.bold}social/{color.green}{color.bold}{name}{color.reset}",htext))
                scraped = scrapefunc(_scrape,url,name,source)
                if(scraped != ""):
                    print()
                    print(scraped)
                threading.Thread(target=ozel_scrape,args=(url,username)).start()
                return {name:url}