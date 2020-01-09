def find_ans(a,b,c,d):
    if a==0 and b==0:
        if d==c+1:
            str_="2 3 "*c
            str_="3 "+str_
            print("YES")
            print(str_)
            return
    elif d==0 and c==0:
        if a-1==b:
            str_="0 1 "*b
            str_=str_+"0"
            print("YES")
            print(str_)
            return
        
    if a>b or d>c:
        print("NO")
        return

    str_left="0 1 "*a
    b=b-a

    str_right="2 3 "*d
    c=c-d
    
    str_val="2 1 "*min(b,c)
    b,c=b-min(b,c),c-min(b,c)

    if b>1 or c>1:
        print("NO")
        return  
    if b==1:str_left="1 "+str_left
    if c==1:str_right+="2 "

    result=str_left+str_val+str_right
    print("YES")
    print(result)



def main():
    values=input()
    values=values.split(" ")
    find_ans(int(values[0]),int(values[1]),int(values[2]),int(values[3]))

main()


