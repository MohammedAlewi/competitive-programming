#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void subtraction(char *input1,char *input2,char *out);
void add(char *input1,char *input2,char *out);
void compliment_num(char *negative_number,char *buffer,int len,int ne_len);
int main(){
    char *negative_number,*positive_number,*bigger_number,*smaller_number;
    char input1[200];
    char input2[200];
    char out[200];
    printf(" >>");

    scanf("%s",input1);

    printf(" >>");
    scanf("%s",input2);
    
    negative_number= input1[0]=='-'?input1:input2;
    positive_number= input1[0]!='-'?input1:input2;

    bigger_number=strlen(negative_number)-1>strlen(positive_number)?negative_number:positive_number;
    smaller_number=strlen(negative_number)-1<strlen(positive_number)?negative_number:positive_number;
    


    subtraction(input1,input2,out);
    printf("%s\n",out);
    return 0;
}

void add(char *input1,char *input2,char *out){
    int len1=strlen(input1);
    int len2=strlen(input2);
    
    int length=0;
    int carry=0;
    if (len1>len2){
        length=len1;
    }else{
        length=len2;
    }
    int i ;
    for ( i = 0; i < length; i++){
        int x=0,y=0,over,over2;
        if((len1-1-i)>=0)x=(input1[len1-1-i])-'0';
        if((len2-1-i)>=0)y=(input2[len2-1-i])-'0';

        if(carry<1) out[length-i]=(char)(x+y)%10 +'0';
        else out[length-i]=(char)(x+y+carry)%10 +'0'; 

        carry=(x+y+carry)/10;              
    }
    out[length-i]=carry+'0';
    out[length+1]='\0'; 
}

void subtraction(char *input1,char *input2,char *out){
    char *negative_number,*positive_number;
    
    negative_number= input1[0]=='-'?input1:input2;
    positive_number= input1[0]!='-'?input1:input2;

    int negative_number_index=  strlen(negative_number);
    int length= (strlen(negative_number)-1>strlen(positive_number))?
            strlen(negative_number)-1:strlen(positive_number);

    negative_number[0]='0';
    char buffer[200];
    compliment_num(negative_number,buffer,length,negative_number_index);

    add(buffer, positive_number,out);
    out[strlen(out)-length-1]='0';
}


void compliment_num(char *negative_number,char *buffer,int len,int ne_len){
    char one[10];
    one[0]='1';one[1]='\0';

    int i;
    int carry=0;
    for ( i = 0; i < len; i++){
        int x=0,y=0,over,over2; //
        if((ne_len-i-1)>=0) x=(negative_number[ne_len-1-i])-'0';
        buffer[len-i]=(char)(9-x) +'0';             
    }
    buffer[len-i]='0';
    buffer[len+1]='\0';
    add(buffer,one,buffer);
}