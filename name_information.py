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

result_name = []
result_type = []
result_index = []
result_price = []
result_infor = []
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
        # print(name)
        headinfor = data.findAll('td', {'class': 'factsheet-noline'})
        type = headinfor[1].text.replace("\n", "").replace("\r", "").replace("\t", "").replace(" ", "")
        result_type.append(type)
        index = headinfor[2].text.replace("\n", "").replace("\r", "").replace("\t", "").replace(" ", "")
        result_index.append(index)
        # print(type)
        # print(index)
        infor = data.findAll('td', {'class': 'factsheet'})
        price = float(infor[0].text)
        result_price.append(price)
        # print(price)
        n = data.text
        k = n.find("ลักษณะธุรกิจ")
        j = n.find("ผู้ถือหุ้นรายย่อย")
        information = n[k:j]
        information = information.replace("\n", "").replace("\r", "").replace("\t", "").replace(" ", "")
        result_infor.append(information)
        # print(information)

        return (result_name, result_type, result_index, result_price, result_infor)
    except:
        result_name.append("-")
        result_type.append("-")
        result_index.append("-")
        result_price.append("-")
        result_infor.append("-")
        return (result_name, result_type, result_index, result_price, result_infor)





for symbol in allsymbol:
    checkname(symbol)
excelfile = Workbook()
sheet = excelfile.active
header = ['SYMBOL','NAME','TYPE','INDEX',"PRICE",'INFORMATION']
sheet.append(header) #เพิ่มค่าเข้าไปทั้งเเเถว
for s,a,b,c,d,e in  zip(allsymbol,result_name,result_type,result_index,result_price,result_infor):
    sheet.append([s,a,b,c,d,e])
excelfile.save("stock.xlsx")
