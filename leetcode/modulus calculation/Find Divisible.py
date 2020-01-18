def runner():
    iters=input()
    for i in range(int(iters)):
        values=input()
        a=values.split()[0]
        b=int(a)*2
        print(a,b)
runner()