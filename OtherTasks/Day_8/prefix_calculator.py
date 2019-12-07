def compute(int1,op,int2):
    if(op=='*'): return int(int1)*int(int2)
    elif(op=='/'): return int(int1)/int(int2)
    elif(op=='-'): return int(int1)-int(int2)
    elif(op=='+'): return int(int1)+int(int2)

def calculate(input):
    stack=input.split()
    while(len(stack)>2):
        int1=stack.pop()
        int2=stack.pop()
        op=stack.pop()
        result=compute(int2,op,int1)
        stack.insert(len(stack)-1,result)
    return stack[0]

print(calculate("+ 4 * 3 / 12  3"))