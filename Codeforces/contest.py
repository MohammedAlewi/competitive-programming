def main(val):
    l=list(val)
    result=""
    for i in range(len(val)-1):
        if val[i]=='?': 
            val= val[:i]+get_val(i,val)+ (val[i+1:] if(i+1<len(val)) else "")
            continue
        elif(val[i]==val[i+1]):
            print(-1);return
    if(val[len(val)-1]=='?'):
        val=val[:len(val)-1]+get_val(len(val)-1,val)
    print(val)
def get_val(i,val):
    d=['a','b','c']
    if(i>0 and len(val)-1==i) or (i>0 and val[i+1]=='?'): 
        try:
            d.remove(val[i-1]) 
        except: pass
        return d[0]
    elif(i>0 and val[i+1]!='?'):
        try:
            d.remove(val[i+1])
            d.remove(val[i-1]) 
        except: pass
        return d[0]
    elif(i==0):
        try:
            d.remove(val[i+1]) 
        except: pass
        return d[0]
 
def runner():
    val=input()
    l=[]
    for i in range(len(val)):
        ans=input()
        l.append(ans)
    for i in l:
        main(i)

runner()