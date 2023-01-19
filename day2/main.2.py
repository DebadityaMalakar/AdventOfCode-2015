f=open("input.txt","r")
blocks=[]
intnums=[]
r=[]
for i in f.read().split("\n"):
    blocks.append(i)
    
for j in blocks:
    #print(j.split("x"))
    x=int(j.split("x")[0])
    y=int(j.split("x")[1])
    z=int(j.split("x")[2])
    m=[]
    m.append(x)
    m.append(y)
    m.append(z)
    intnums.append(m)
    #print("\n")
for k in intnums:
    Min=min(k)
    a=k
    a.remove(Min)
    Min2=min(a)
    b=(Min+Min+Min2+Min2)
    r.append(b)
print(sum(r))