f=open("input.txt","r")
blocks=[]
nums=[]
intnums=[]
Areas=[]
for i in f.read().split("\n"):
    blocks.append(i)
    
for j in blocks:
    print(j.split("x"))
    x=int(j.split("x")[0])
    y=int(j.split("x")[1])
    z=int(j.split("x")[2])
    m=[]
    m.append(x)
    m.append(y)
    m.append(z)
    intnums.append(m)
    print("\n")
for k in intnums:
    area=(2*k[0]*k[1])+(2*k[1]*k[2])+(2*k[2]*k[0])
    Min=min(k)
    a=k
    a.remove(Min)
    Min2=min(a)
    b=(Min*Min2)+area
    Areas.extend([b])

print(sum(Areas))