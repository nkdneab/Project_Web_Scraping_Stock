from openpyxl import Workbook

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
    excelfile.save("stock.xlsx")
