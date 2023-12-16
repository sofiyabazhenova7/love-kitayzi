a = "12, 13, 12, 54, 3"
a=a.split(', ')
b = 3
c = []
def Vika(a,b,c):
    for i in range(len(a)):
        a[i]=int(a[i])
        k = a[i]*b
        c.append(k)
    print(c)
    
Vika(a,b,c)      
    

    

            