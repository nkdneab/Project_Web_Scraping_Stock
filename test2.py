from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
url = 'https://www.set.or.th/set/companyhighlight.do?symbol=M&ssoPageId=5&language=th&country=TH'
webopen = urlopen(url)
page_html = webopen.read()
webopen.close()
data = soup(page_html, 'html.parser')
priceallrow = data.findAll('td')
np = len(priceallrow)
c=0
for n in range(np):
    try:
        x = str(priceallrow[n].text.replace(',', ''))  # ถ้าเข้าอันนี้เป็นเลข
        check = float(x)
        print(priceallrow[n].text)
        c+=1


    except:  # ถ้าเข้าอันนี้เป็นตัวอักษร
        print(priceallrow[n].text)
        if c>0:
            print(c)
        c=0
