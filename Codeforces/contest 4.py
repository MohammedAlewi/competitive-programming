def main(MOVE):
    r=MOVE.count('R')
    l=MOVE.count('L')
    d=MOVE.count('D')
    u=MOVE.count('U')
    x=min([l,r])
    y=min([u,d])
    if y==0:
        x=min([x,1])
    if x==0:
        y=min([y,1])
    ans=['R']*x
    ans+=['U']*y
    ans+=['L']*x
    ans+=['D']*y
    print((x+y)*2)
    print("".join(ans))


def runner():
    val=input()
    x=[]
    for i in range(int(val)):
        ans=input()
        x.append(ans)
    for i in range(int(val)):
        main(x[i])

runner()
