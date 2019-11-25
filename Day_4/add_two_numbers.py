def add_int(str1,str2):
    str1="0"*(len(str2)-len(str1))+str1;
    str2="0"*(len(str1)-len(str2))+str2;
    length=len(str1)
    out=[0]*(length+1)
    carry=0
    for i in range(length):
        if(carry<1):out[length-i]=(int(str1[length-1-i])+int(str2[length-1-i]))%10
        else: out[length-i]=(int(str1[length-1-i])+int(str2[length-1-i])+carry)%10
        carry=(int(str1[length-1-i])+int(str2[length-1-i])+carry)//10  
    out[0]=carry;
    return remove_zero(to_str(out))

def add(str1,str2):
    str1=str1.split('.')
    str2=str2.split('.')
    result=add_int(str1[0],str2[0])
    
    decimal_1=str1[1] if (len(str1)>1) else "0"
    decimal_2=str2[1] if (len(str2)>1) else "0"
    
    decimal_1=decimal_1+"0"*(len(decimal_2)-len(decimal_1));
    decimal_2=decimal_2+"0"*(len(decimal_1)-len(decimal_2));

    result+='.'+add_int(decimal_1,decimal_2)
    return result
def main():
    input1=input("num 1 >>");
    input2=input("num 2 >>");

    print(add(input1,input2))

main()