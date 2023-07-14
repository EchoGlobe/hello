file =open ('flames1.txt','a')
file.write('\n............................................\n')
a=input('Enter the name:')
b=input('Enter the name:')
file.write(a+'  ')
file.write(b+'  ===>')
c='F,L,A,M,E,S'.split(',')
d=[];e=[]
a=a.upper()    
b=b.upper()
for i in a:
    if i!=' ':d.append(i)
for j in b:
    if i!=' ':e.append(j)
g=e.copy()

for I in d:
    if I in e:e.remove(I)
    
for I in g:
    if I in d:d.remove(I)
    
h=len(d)+len(e)
print(f'{a}={d}\n{b}={e}\ntotal length is {h}')

i=lambda x, y : x // y
j=lambda x, y : x * y
k=lambda x, y : x - y 
print (c)
for I in range (6,1,-1):
    if h!=0:
        l=i(h,I)
        print(l)
        m=j(l,I)
        n=k(h,m)
        z=I-1
        if n == 0:c.pop(z)
        elif n == 1:c.pop(0)
        else:
            p=n-1
            c.remove(c[p])
            for o in range(I-1):
                   q=len(c)
                   c.insert(o,c[p])
                   r=p+1
                   c.pop(r)
                   n=n+1
                   if p == (q-1):break
                   else:p= p+1
        
        if I == 2:
            print (c)
            y=None
            if c[0]=='F':y='is FRIEND to'
            if c[0]=='L':y='is in LOVE with'
            if c[0]=='A':y='has more AFFECTION on'
            if c[0]=='M':y='is going to MARRY '
            if c[0]=='E':y='is ENEMY TO'
            if c[0]=='S': print (f'{a} and {b} are Sisters/Brothers')
            if y!=None:
                z=f'{a} {y} {b}'
                print (z)   
                file.write(z)
            break
        else : print (c)
    else :
        y=f'{a} and {b} are all Relationships'
        print (y)
        file.write(y)
        break