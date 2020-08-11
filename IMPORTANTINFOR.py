from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook

#ตั้งค่าsymbolหรือเรียกใช้ allsymbol
allsymbol=['MK','M']
def Read_all_symbol():
    f=open('All_symbol.text')
    for line in f:
        allsymbol.append(line.strip())
    f.close()
    return (allsymbol)
#Read_all_symbol()


#การสร้าง list ทั้งหมด
result_Total_Assets = []



#FUNCTION
def Total_Assets(symbol,NO): #3-7
    #if NO == 1:#ดึงมาเเค่ปีล่าสุด

    #if NO == 2:

    #if NO == 3:

    #if NO == 4:

    if NO == 5:
        try:
            url = f'https://www.set.or.th/set/companyhighlight.do?symbol={symbol}&ssoPageId=5&language=th&country=TH'
            webopen = urlopen(url)
            page_html = webopen.read()
            webopen.close()
            data = soup(page_html, 'html.parser')
            Asset = data.findAll('td')
            




        except:
            result_Total_Assets.append("-")
            return (result_Total_Assets)





Total_Assets("M",5)