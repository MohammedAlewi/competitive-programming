#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void add(char *input1,char *input2,char *out);
void multiply(char *input1,char *input2,char *out);
int compare(char *input1,char *input2);

int main(){
    char input1[200];
    char input2[200];
    char out[200];
    printf(" >>");

    scanf("%s",input1);

    printf(" >>");
    scanf("%s",input2);
    multiply(input1,input2,out);

    printf("result : %s\n",out);
    return 0;
}

void multiply(char *input1,char *input2,char *out){
    char index[200];
    char out_put[200];
    char inc[10];
    inc[0]='1';
    inc[1]='\0';
    index[0]='1';
    index[1]='\0';
    
    add(index,inc,index);
    
    add(input2,input2,out);
    while(compare(index,input1)==0){  
        add(input2,out,out);
        add(index,inc,index);
    }
}

int compare(char *input1,char *input2){
    int ans=1;
    int len1=strlen(input1)-1;
    int len2=strlen(input2)-1;
    int length=len1>len2? len1:len2;
    for (int i = 0; i <=length; i++){
        //printf("\nout : %c %c",input1[len1-i],input2[len2-i]);
        //1printf("\nn1 :%s n2 :%s comp: %d \n",input1[len1-i]!=input2[len2-i] && ((input1[len1-i])!='0'  && (input1[len2-i])!='0'  ));
        if ((input1[len1-i]!=input2[len2-i] && ((len1-i)>=0 && (len2-i)>=0) )){
           return 0; 
        }
    }
    printf("------- \n");

    return ans;
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
     out[length+1]='\0';
     out[length-i]=carry+'0';


}
