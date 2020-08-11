allsymbol=[]
def Read_all_symbol():
    f=open('wis.txt')
    for line in f:
        allsymbol.append(line.strip())
    f.close()
    return (allsymbol)
Read_all_symbol()
print(allsymbol)