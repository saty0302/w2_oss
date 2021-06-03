def duplicate( a ):
    d={}
    l=[]
    for i in a :
        if i in d :
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i]>1:
            l.append(i)
    return l
            
        
          

print(duplicate([1,2,3,4,5,3]))
