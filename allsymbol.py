from urllib.request import urlopen
import string
from bs4 import BeautifulSoup as soup
m = string.ascii_uppercase
n=[]
for i in m:
    n.append(i)
n.append("NUMBER")
f = open('All_symbol.text', 'w')
for mm in n:
    url = 'https://www.set.or.th/set/commonslookup.do?language=th&country=TH&prefix=' + mm
    webopen = urlopen(url)
    page_html = webopen.read()
    webopen.close()
    data = soup(page_html, 'html.parser')
    name = data.findAll('td')
    n = 0
    while n <= 500:
        try:
            name_text=name[n].text
            name_text = name_text.replace(' ','%20')
            name_text = name_text.replace('&','%26')
            f.write(name_text+'\n')
            n = n + 3
        except:
            break
f.close()






