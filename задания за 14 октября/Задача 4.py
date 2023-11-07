v = 'hghghhghghghghghbbfbfb hfhyfyhfgcb hfhyfhgrvhjxidi gdgtfdvdgcftfrh'
def camel(v):
    a = [' ']
    for i in range(len(v)):
        if v[i] not in a:
           # continue            
            if i % 2 == 0:
                if v[i].islower() == True:
                    print(v[i])
                    v = v[:i] + v[i].swapcase() + v[i+1:]
        
    print(v)
camel(v)