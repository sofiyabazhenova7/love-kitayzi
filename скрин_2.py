a = 'hgbhgbh!!!!njfhbf!!!!???'
def Vika(a):
    b = 0
    c = 0 
    a = list(reversed(a))
    for i in range(len(a)):
        if a[i] == '!':
            b+=1          
        elif a[i] == '?':
            c+=1
        elif a[i] != '!' and a[i] != '?':
            f=i
            break
    m=a[:f]
    if b ==0 and c !=0:
        s=a[f:]
        s.reverse()
        s.append('?')
    if b !=0 and c ==0:
        s=a[f:]
        s.reverse()
        s.append('!')
    if b !=0 and c !=0:
        s=a[f:]
        s.reverse()
        s.append('?!')
    
    
    print(''.join(s))
Vika(a)