#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import urllib
from fake_useragent import UserAgent

query = "купить аирподс"
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"
# URL = "https://www.google.com/search?q=%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C+%D0%BB%D0%BE%D0%B6%D0%B5%D1%87%D0%BA%D1%83&rlz=1C1SQJL_enUA897UA898&oq=%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C+%D0%BB%D0%BE&aqs=chrome.1.69i57j35i39j0l6.2117j0j7&sourceid=chrome&ie=UTF-8"

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

# headers = {"user-agent" : USER_AGENT}


ua = UserAgent()
print(ua.chrome)
headers = {'User-Agent':str(ua.chrome)}
textHtmlPars = requests.get(URL, headers=headers)
print(textHtmlPars)

text = textHtmlPars.text
soup = BeautifulSoup(text, 'html.parser')
citeName= soup("cite")
f = open('test.txt', 'w')
f.write(str(citeName))
f.close()

# txt2222 = "welcome to the jungle"

# x = str(citeName[0]).split('>')
# # x2 = x.split(',')
# print(x)
# # print(x[2])

