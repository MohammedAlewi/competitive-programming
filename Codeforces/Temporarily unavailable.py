    def main(a,b,x,r):
        if (x<b and x>a) or (x>b and x<a):
            if x-r<min([a,b]):
                l= abs(max([a,b])-x) -r
                l= 0 if l<0 else l
                print(l)
            elif x+r>max([a,b]):
                l= abs(min([a,b])-x) -r
                l= 0 if l<0 else l
                print(l)
            else:
                left=abs(b-a)-2*r
                left= 0 if left<0 else left
                print(left)
                return
        elif (x>=b and x>=a):
            if x-r<b or x-r<a:
                l=abs(b-a)-(r-abs(x-max([b,a])))
                l= 0 if l<0 else l
                print(l)
            else:
                print(abs(b-a))
        elif (x<=b and x<=a):
            if x+r>min([b,a]):
                l=abs(b-a)-(r-abs(x-min([b,a])))
                l= 0 if l<0 else l
                print(l)
            else:
                print(abs(b-a))
    def runner():
        val=input()
        for i in range(int(val)):   
            a=input()
            a=a.split(" ")
            main(int(a[0]),int(a[1]),int(a[2]),int(a[3]))
    runner()