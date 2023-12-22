a= [[1,2,3],[5,6,7],[5,5,5],[7,3,5]]
c=0
for i in range(len(a)):
    b = a[i][0]*a[i][1]*a[i][2]
    c +=b
print(c)   
