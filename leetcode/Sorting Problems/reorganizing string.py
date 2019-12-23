def reorganize(str_val):
    d=dict()
    for i in str_val:
        if(d.get(i)==None):d[i]=1
        else:d[i]+=1
    val=list(d.values())
    val.sort()
    if(val[-1]*2-sum(val)>=2):return ""
    result=""

    for i in range(len(str_val)):
        v=max_val(d)
        result+=v+max_val(d,v)
        i+=2
    return result

def max_val(d,ex=None):
    result=list(d.keys())[0] if list(d.keys())[0]!=ex else list(d.keys())[1]
    for i in d.keys():
        if d.get(i)>d.get(result) and i!=ex:result=i
    d[result]-=1
    return result if d[result]>-1 else ''

print(reorganize("eeeeedddddbbbcccaaaa"))