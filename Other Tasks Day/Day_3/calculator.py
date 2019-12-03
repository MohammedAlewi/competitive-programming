#--------------- common functions-----------------#

def to_str(out):
    result=""
    for i in out:result+=str(i);
    return result;

def remove_zero(str):
    for i in range(len(str)):
        if(int(str[i])!=0): return str[i:];
    return "0";

#-----------------multiplication-----------------#

def mul(str1,str2):
    out=0;
    for i in range(0,len(str1)):
        out+=int(str1[i])*int(str2[len(str1)-1-i])
    return out;

def result(out):
    length=len(out)
    for i in range(length):
        if(out[length-1-i]/10>1 and length-2-i>=0):
            out[length-2-i]=out[length-2-i]+out[length-1-i]//10;
            out[length-1-i]=out[length-1-i]%10;
    return out;

def _multiply(str1,str2):
    length=len(str1);
    out=[0]*(length*2-1)
    for i in range(1,2*length):
        if(i<=length):out[i-1]=mul(str1[0:i],str2[0:i]); 
        else:out[i-1]=mul(str1[i-length:length],str2[i-length:length]);
    return to_str(result(out))

def multiply(str1,str2):
    str1="0"*(len(str2)-len(str1))+str1;
    str2="0"*(len(str1)-len(str2))+str2;
    return _multiply(str1,str2)

#--------------------- ADD ---------------------
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

#------------------- subtraction------------------

def compare(str1,str2):
    for i in range(len(str1)):
        if(int(str1[i])<int(str2[i])):return True;
        elif(int(str1[i])>int(str2[i])):return False;
    return True

def compliment(str_val):
    out=[9-int(input) for input in str_val]
    out=add(to_str(out),"1").split('.')[0]
    return out;

def subtract(str1,str2):
    neg= str1[1:] if(str1[0]=='-') else str2[1:];
    pos= str1 if(str1[0]!='-') else str2;
    neg="0"*(len(pos)-len(neg))+neg;
    pos="0"*(len(neg)-len(pos))+pos;

    if compare(neg,pos):
        out=add(compliment(neg),pos).split('.')[0]
        return out[len(out)-len(neg):]
    else:
        out=add(compliment(pos),neg).split('.')[0]
        return '-'+out[len(out)-len(neg):]

#------------------ division --------------#
def decimal_part(divident,divier):
    out="0"
    decimal_point=0
    divident=multiply(divident,"1000");
    divident="0"*(len(divier)-len(divident))+divident;
    divier="0"*(len(divident)-len(divier))+divier;
    while(compare(divier,divident)):
        out=add(out,"1");
        divident=subtract(divident,divier) 
        if(compare(divier,divident)==False and decimal_point<3):
            divident=multiply(divident,"10");
            decimal_point+=1
    return out

def divide(divident,divier):
    divident="0"*(len(divier)-len(divident))+divident;
    divier="0"*(len(divident)-len(divier))+divier;
    result="0";
    while(compare(divier,divident)):
        result=add(result,"1");
        divident=subtract(divident,'-'+divier)
    if(remove_zero(divident)!="0"):
        result=add(result,"0."+decimal_part(divident,divier))
    return result
    
#------------------ Test-------------------#

def main():
    # enter the positive Integer then the sign (do not mix numbers and signs!)
    # for the addition you can add decimal points also!!
    input1=input("num 1 >>");
    oprator=input("(-,+,/,x) >>")
    input2=input("num 2 >>");

    if(oprator=='-'):
        print(subtract(input1,'-'+input2))
    elif(oprator=='/'):
        print(divide(input1,input2))
    elif(oprator=='+'):
        print(add(input1,input2))
    elif(oprator=='x'):
        print(multiply(input1,input2))

main()