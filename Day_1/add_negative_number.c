#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void subtraction(char *input1,char *input2,char *out);
void add(char *input1,char *input2,char *out);
int main(){
    char input1[200];
    char input2[200];
    char out[200];
    printf(" >>");

    scanf("%s",input1);

    printf(" >>");
    scanf("%s",input2);
    //add(input1,input2,out);
    subtraction(input1,input2,out);
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
        else out[length-i]=(char)(x+y)%10+carry +'0'; 
  
        carry=(x+y)/10;              
    }
    out[length-i]=carry+'0';
    out[length+1]='\0';
    
    printf("%s\n",out);
    
}

void subtraction(char *input1,char *input2,char *out){
    int len1=strlen(input1);
    int len2=strlen(input2);
    int length= (len1>len2)?len1:len2;
    char *negative_number;
    
    negative_number= input1[0]=='-'?input1:input2;
    int negative_number_index= len2>len1? len1:len2;
    
    negative_number[0]='0';
    char buffer[200];

    int i;
    int carry=0;
    for ( i = 0; i < length; i++){
        int x=0,y=0,over,over2;
        if((negative_number_index-1-i)>=0) x=(negative_number[negative_number_index-1-i])-'0';
        if(i==0) out[length-i]=(char)(9-y+1) +'0';
        // if((len1-1-i)>=0)x=(input1[len1-1-i])-'0';
        // if((negative_number_index-1-i)>=0)y=(negative_number[negative_number_index-1-i])-'0';

        // if(x-y-carry>0){
        //     buffer[length-i]=(char)(x-y-carry) +'0';
        //     carry=0;
        // } 
        // else {
        //     buffer[length-i]=(char)(x+10-y-carry) +'0';
        //     carry=1;
        // } 
  
                  
    }
    if(carry==1)
        out[length-i]='-';
    else
        out[length-i]='0';
    out[length-i]='\0';
    //printf("%s\n",negative_number);
    printf("here %s\n",buffer);
}