wang=[]
real=[]
f=open('wis.txt')
for line in f:
    real.append(line.strip())
f.close()
ff=open('wiss')
for line in ff:
    wang.append(line.strip())
ff.close()
#print(len(wang),len(real))
for r in real:
    n=0
    for w in wang:
        if r == w:
            n+=1
    print(r,n)


