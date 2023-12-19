a = [1, 2, 4, 3]
r=0
def Olesya(a,r): 
    if sum(a)%3==0:
        for i in range(len(a)):
            if a[i]<=sum(a)/3:
                r+=1
    if r == len(a):
        print('Деты будут не бомжами')
    else: 
        print('Дети умрут от голода')
Olesya(a,r)
            
