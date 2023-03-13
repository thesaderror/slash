from core.scrape import *
from profiles.autoimport import *
def split_extra(name,txt):
    out = ""
    if(name=="Name"):
        txt = txt.split()
        for i in range(0,len(txt)):
            out+=txt[i]+" "
        return out  
    elif(name=="Bio"):
        txt = txt.split()
        for i in range(0,len(txt)):
            out+=txt[i]+" "
        return out  
    else:
        return txt

def scrapefunc(_scrape,url,name,source):
    scraped = ""
    lsc = len(_scrape)
    #print(_scrape)
    for sc in range(0,lsc):
        scrape_cname = _scrape[f"{sc}"]["cname"]
        scrape_name = _scrape[f"{sc}"]["name"]
        if(scrape_cname=="span"):
            scrape_text = span(source, _scrape[f"{sc}"]["class"])                                
            if(scrape_text!=None):
                scrape_text = split_extra(scrape_name,scrape_text)
                parse(scrape_name,scrape_text,name,url)
                scraped+=(f"""[{color.green}{color.underline}{name}{color.reset}] {color.bold}{color.blue}{scrape_name}{color.reset} : {color.green}{color.underline}{scrape_text}{color.reset}\n""")
        elif(scrape_cname=="a"):
            scrape_text = ahead(source, _scrape[f"{sc}"]["class"])                                
            if(scrape_text!=None):
                scrape_text = split_extra(scrape_name,scrape_text)            
                parse(scrape_name,scrape_text,name,url)
                scraped+=(f"""[{color.green}{color.underline}{name}{color.reset}] {color.bold}{color.blue}{scrape_name}{color.reset} : {color.green}{color.underline}{scrape_text}{color.reset}\n""")

        elif(scrape_cname=="div"):
            scrape_text = div(source, _scrape[f"{sc}"]["class"])                                
            if(scrape_text!=None):
                scrape_text = split_extra(scrape_name,scrape_text)               
                parse(scrape_name,scrape_text,name,url)
                scraped+=(f"""[{color.green}{color.underline}{name}{color.reset}] {color.bold}{color.blue}{scrape_name}{color.reset} : {color.green}{color.underline}{scrape_text}{color.reset}\n""")
        
        elif(scrape_cname=="h1"):

            scrape_text = h1(source, _scrape[f"{sc}"]["class"])                                
            if(scrape_text!=None):
                scrape_text = split_extra(scrape_name,scrape_text)           
                parse(scrape_name,scrape_text,name,url)
                scraped+=(f"""[{color.green}{color.underline}{name}{color.reset}] {color.bold}{color.blue}{scrape_name}{color.reset} : {color.green}{color.underline}{scrape_text}{color.reset}\n""")

        elif(scrape_cname=="p"):

            scrape_text = phead(source, _scrape[f"{sc}"]["class"])                                
            if(scrape_text!=None):
                scrape_text = split_extra(scrape_name,scrape_text)           
                parse(scrape_name,scrape_text,name,url)
                scraped+=(f"""[{color.green}{color.underline}{name}{color.reset}] {color.bold}{color.blue}{scrape_name}{color.reset} : {color.green}{color.underline}{scrape_text}{color.reset}\n""")

        elif(scrape_cname=="section"):
            scrape_text = section(source, _scrape[f"{sc}"]["class"])                                
            if(scrape_text!=None):
                scrape_text = split_extra(scrape_name,scrape_text)           
                parse(scrape_name,scrape_text,name,url)
                scraped+=(f"""[{color.green}{color.underline}{name}{color.reset}] {color.bold}{color.blue}{scrape_name}{color.reset} : {color.green}{color.underline}{scrape_text}{color.reset}\n""")
    return scraped
