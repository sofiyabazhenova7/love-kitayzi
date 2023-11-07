a = 'vcgcggghffhhyyh (bbdgbcgcbcgbsbh) gdhbc gcdcvdtvcb (dgghbvb(fhhvbbv)hfhfhvb) dgdfghhvnjcdjjhch'
def shortener(a):
    n = a.count('(')
    print(n)
    for i in range(n): 
       if (a[:a.find('(')] + a[a.find(')')+1:]).find("(") > 0: 
          a = (a[:a.find('(')] + a[a.find(')')+1:]).replace('(', ' ')
          a = (a[:a.find('(')] + a[a.find(')')+1:]).replace(')', ' ')
       a = a[:a.find('(')] + a[a.find(')')+1:]
       
    print(a)
    
shortener(a)