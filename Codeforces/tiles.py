def main():
    x=int(input(""))
    l=[]
    for i in range(x):
        y=input()
        l.append(y)
    calculate(l)
def calculate(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j]=='.' and not valid(l,i,j):
                print("NO")
                print(l)
                return
    print("YES")
def valid(l,i,j):
    l[i]=l[i][:j]+'#'+l[i][j+1:]
    for k in range(-1,2):
        print(k,j,l[i][j+k])
        if j+k>=0 and k+j<len(l[i+1]) and l[i+1][j+k]=='.':
             l[i+1]=l[i+1][:j+k]+'#'+l[i+1][j+k+1:]
        else: return False
    if i+2<len(l) and l[i+2][j]=='.':
        l[i+2][j]='#'
        l[i+2]=l[i+2][:j]+'#'+l[i+2][j+1:]
        return True
    return False
main()