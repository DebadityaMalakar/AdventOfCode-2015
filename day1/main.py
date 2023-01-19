x=0
z=[]
c=-1
f=open("input.txt",'r')
for i in f.read():
    if x==-1:
        print(z[c])
        break
    else:
        if i == "(":
            x+=1
            c += 1
            z.append(c)
        elif i == ")":
            x -=1
            c +=1 
            z.append(c)
        else:
            c +=1
            z.append(c)
f.close()
print(x)