def main(cmd):
    l=cmd.count("L")
    r=cmd.count("R")
    print(l+r+1)
def runner():
    val=input()
    cmd=input()
    main(cmd)
runner()
