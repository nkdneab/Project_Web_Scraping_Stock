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
result_name = []
result_type = []
result_index = []
result_price = []
result_infor = []
TYPEstatement=[]
AccountingPeriod=[]
STATUSstatement=[]
URLFULLstatement=[]


#FUNCTION
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


def checkname(symbol):
    try:
        url = f'https://www.set.or.th/set/factsheet.do?symbol={symbol}&ssoPageId=3&language=th&country=TH'
        webopen = urlopen(url)
        page_html = webopen.read()
        webopen.close()
        data = soup(page_html, 'html.parser')
        name = data.findAll('td', {'class': 'factsheet-heading2'})
        name = name[0].text
        result_name.append(name)
    except:
        result_name.append("-")
        return (result_name)


def checktype(symbol):
    try:
        url = f'https://www.set.or.th/set/factsheet.do?symbol={symbol}&ssoPageId=3&language=th&country=TH'
        webopen = urlopen(url)
        page_html = webopen.read()
        webopen.close()
        data = soup(page_html, 'html.parser')
        headinfor = data.findAll('td', {'class': 'factsheet-noline'})
        type = headinfor[1].text.replace("\n", "").replace("\r", "").replace("\t", "").replace(" ", "")
        result_type.append(type)
    except:
        result_type.append("-")
        return (result_type)


def checkindex(symbol):
    try:
        url = f'https://www.set.or.th/set/factsheet.do?symbol={symbol}&ssoPageId=3&language=th&country=TH'
        webopen = urlopen(url)
        page_html = webopen.read()
        webopen.close()
        data = soup(page_html, 'html.parser')
        headinfor = data.findAll('td', {'class': 'factsheet-noline'})
        index = headinfor[2].text.replace("\n", "").replace("\r", "").replace("\t", "").replace(" ", "")
        result_index.append(index)
    except:
        result_index.append("-")
        return (result_index)


def checkprice(symbol):
    try:
        url = f'https://www.set.or.th/set/factsheet.do?symbol={symbol}&ssoPageId=3&language=th&country=TH'
        webopen = urlopen(url)
        page_html = webopen.read()
        webopen.close()
        data = soup(page_html, 'html.parser')
        infor = data.findAll('td', {'class': 'factsheet'})
        price = float(infor[0].text)
        result_price.append(price)
    except:
        result_price.append("-")
        return (result_price)


def checkinfor(symbol):
    try:
        url = f'https://www.set.or.th/set/factsheet.do?symbol={symbol}&ssoPageId=3&language=th&country=TH'
        webopen = urlopen(url)
        page_html = webopen.read()
        webopen.close()
        data = soup(page_html, 'html.parser')
        n = data.text
        k = n.find("ลักษณะธุรกิจ")
        j = n.find("ผู้ถือหุ้นรายย่อย")
        information = n[k:j]
        information = information.replace("\n", "").replace("\r", "").replace("\t", "").replace(" ", "")
        result_infor.append(information)
    except:
        result_infor.append("-")
        return (result_infor)

#################################EXCEL
def Write_excel():
    for symbol in allsymbol:
        #ใส่ funtion ที่ต้องการตรวจสอบ
        checkname(symbol)
        checktype(symbol)
        checkindex(symbol)
        checkprice(symbol)
        checkinfor(symbol)

    excelfile = Workbook()
    sheet = excelfile.active

    #ใส่หัวเรื่องให้ตรงกับสิ่งที่ต้องการเช็ค
    header = ['SYMBOL', 'NAME', 'TYPE', 'INDEX', "PRICE", 'INFORMATION']
    sheet.append(header)  # เพิ่มค่าเข้าไปทั้งเเเถว

    #ใส่ค่าที่ retrun ออกมาจาก funtion ลงไป
    for s, a, b, c, d, e in zip(allsymbol, result_name, result_type, result_index, result_price, result_infor):
        sheet.append([s, a, b, c, d, e])

    #ตั้งชื่อ file
    excelfile.save("stock2.xlsx")
Write_excel()