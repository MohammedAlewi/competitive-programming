#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void add(char *input1,char *input2,char *out);
void multiply(char *input1,char *input2,char *out);
int main(){
    char input1[200];
    char input2[200];
    char out[200];
    printf(" >>");

    scanf("%s",input1);

    printf(" >>");
    scanf("%s",input2);
    multiply(input1,input2,out);
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

void multiply(char *input1,char *input2,char *out){
    char index[200];
    char out_put[200];
    char inc[0];
    inc[0]='1';
    index[0]='1';
    index[1]='\0';
   add(index,inc,index);
    // while(strcmp(index,input1)==0){

    // }
}