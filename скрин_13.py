a = " Люблю отчизну я    , но   странно "
b = ' '
for i in range(0, 10):
    for j in range(0, i):
        b = b + ' '
     
    a = a.replace(b, '')  
print(a)