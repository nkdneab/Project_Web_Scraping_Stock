from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook

allsymbol=[]
def Read_all_symbol():
    f=open('All_symbol.text')
    for line in f:
        allsymbol.append(line.strip())
    f.close()
    return (allsymbol)
Read_all_symbol()

TYPEstatement=[]
AccountingPeriod=[]
STATUSstatement=[]
URLFULLstatement=[]

def information_statement(symbol):
    def TYPE_Statement():
        try:
            url = f'https://www.set.or.th/set/companyfinance.do?type=balance&symbol={symbol}&language=th&country=TH'
            webopen = urlopen(url)
            page_html = webopen.read()
            webopen.close()
            data = soup(page_html, 'html.parser')
            find = data.findAll('table', {'class': 'table table-hover table-info'})
            m = find[0].text
            m = m.split()

            TYPEstatement.append(m[1])
        except:
            TYPEstatement.append("-")
        return (TYPEstatement)

    def AccountingPeriod_Statement():
        try:
            url = f'https://www.set.or.th/set/companyfinance.do?type=balance&symbol={symbol}&language=th&country=TH'
            webopen = urlopen(url)
            page_html = webopen.read()
            webopen.close()
            data = soup(page_html, 'html.parser')
            find = data.findAll('table', {'class': 'table table-hover table-info'})
            n = find[1].text
            n = n.split()
            AccountingPeriod.append(n[1])
        except:
            AccountingPeriod.append("-")
        return (AccountingPeriod)

    def Status_Statement():
        try:
            url = f'https://www.set.or.th/set/companyfinance.do?type=balance&symbol={symbol}&language=th&country=TH'
            webopen = urlopen(url)
            page_html = webopen.read()
            webopen.close()
            data = soup(page_html, 'html.parser')
            find = data.findAll('table', {'class': 'table table-hover table-info'})
            m = find[0].text
            m = m.split()
            STATUSstatement.append(m[3])
        except:
            STATUSstatement.append("-")
        return (STATUSstatement)

    def URL_Statement():
        try:
            url = f'https://www.set.or.th/set/companyfinance.do?type=balance&symbol={symbol}&language=th&country=TH'
            webopen = urlopen(url)
            page_html = webopen.read()
            webopen.close()
            data = soup(page_html, 'html.parser')
            find = data.findAll('table', {'class': 'table table-hover table-info'})
            o = find[1]
            find2 = str(o)
            find2 = find2.split("<a")
            find3 = find2[1].split('"')
            URL = find3[1]
            URLFULLstatement.append(URL)
        except:
            URLFULLstatement.append("-")
        return (URLFULLstatement)
    TYPE_Statement()
    AccountingPeriod_Statement()
    Status_Statement()
    URL_Statement()





















def Write_excel():
    for symbol in allsymbol:
        #ใส่ funtion ที่ต้องการตรวจสอบ
        information_statement(symbol)

    excelfile = Workbook()
    sheet = excelfile.active

    #ใส่หัวเรื่องให้ตรงกับสิ่งที่ต้องการเช็ค
    header = ['SYMBOL', 'TYPE', 'ACCOUNTING PERIOD', 'STATUS', "URL"]
    sheet.append(header)  # เพิ่มค่าเข้าไปทั้งเเเถว

    #ใส่ค่าที่ retrun ออกมาจาก funtion ลงไป
    for a, b, c, d, e in zip(allsymbol, TYPEstatement,AccountingPeriod,STATUSstatement,URLFULLstatement):
        sheet.append([a, b, c, d, e])

    #ตั้งชื่อ file
    excelfile.save("STATEMENT.xlsx")
Write_excel()













