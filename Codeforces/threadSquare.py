    import math
    def main():
        l=input()
        l=l.split()
        ans=math.ceil(int(l[0])/int(l[2]))*math.ceil(int(l[1])/int(l[2]))
        print(ans)
     
    if __name__=="__main__":
        main()

