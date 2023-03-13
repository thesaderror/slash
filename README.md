# [Slash](https://github.com/theahmadov/slash)

Slash is **Automated Osint Tool** that allows you to **OSINT** people by their username.

### Slash OSINT Modules :
```python
|__Checker                                                    |
|  |                                                          |
|  |__Social Media Profile Check (+187)                       |
|  |__Forums Profile Check (+30)                              |
|  |__Leak Check (Username,Email-Adress)                      |
|                                                             |
|__Search                                                     |
|  |                                                          |
|  |__Pastebin Paste Search                                   |
|  |__Github Commit Search                                    |
|                                                             |
|__Extract Scrape                                             |
|  |                                                          |
|  |__Phone Number Extract      (From Bios,Raw Texts)         |
|  |__Mail Extractor            (From Bios,Raw Texts)         |
|  |__Bio Scraper               (Social Media)                |
|  |__Name Scraper              (Social Media)                |
|  |__Location Scraper          (Social Media)                |
|  |__Education Info Scraper    (Social Media)                |
|  |__Personal Website Scraper  (Social Media)                |
|__|__________________________________________________________|
```

## What's new in the X version ?
- [x] Speed dramatically increased
- [x] Export the last result to JSON file (results.json)
- [ ] Use as external module (TODO)


## Installation

```
git clone https://github.com/theahmadov/slash
cd slash
pip install -r requirements.txt
python slash.py help
```

## Usage & Syntax

* Username Syntax : **python slash.py username**
* Mail Adress Syntax : **python slash.py mail_adress**

* Example : 
```
python slash.py theahmadov
```
<h1 align="center">
  <img src="https://raw.githubusercontent.com/theahmadov/slash/main/images/1.png">
</h1>
<h1 align="center">
  <img src="https://github.com/theahmadov/slash/blob/main/images/2.png?raw=true">
</h1>

### Credits
Links of social.json : [sherlock-project](https://github.com/sherlock-project/sherlock/)


![](https://visitor-badge.glitch.me/badge?page_id=thesaderror.slash)
