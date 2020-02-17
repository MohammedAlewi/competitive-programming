def recv(n,m,s1,s2,vals):
    
    if ((n,m)) in vals:
        return vals[(n,m)]
    if n<0 or m<0:
        if n>=0:
            strv=s1[:n]+s1[n]
        elif m>=0:
            strv=s2[:m]+s2[m]
        vals[(n,m)]=max(n,m),strv
        return vals[(n,m)]
    
    if s1[n]==s2[m]:
        rc=recv(n-1,m-1,s1,s2,vals)
        strv=rc[1]+s1[n]
        vals[(n,m)]=rc[0]+1,strv
        return vals[(n,m)]
    else:
        r1=recv(n-1,m,s1,s2,vals)
        r2=recv(n,m-1,s1,s2,vals)

        strv1=r1[1]+s1[n]
        strv2=r2[1]+s2[m]
        if r1<r2:
            vals[(n,m)]=min(r1[0],r2[0])+1,strv1
            return vals[(n,m)]
        else:
            vals[(n,m)]=min(r1[0],r2[0])+1,strv2
            return vals[(n,m)]



s1='ABCBDAB'
s2='BDCABA'

vals={}

x=recv(len(s1)-1,len(s2)-1,s1,s2,vals)

print(x[0],x[1])