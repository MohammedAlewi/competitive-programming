#include <stdio.h>
#include <stdlib.h>
void print_space(int original,int limit);
void print_star(int limit);

int main(){
    int input;
    scanf("%d",&input);
    for (int col = 1; col <= input; col++){
        // print space 
        print_space(input,col);
        // print star
        print_star(col);

        printf("\n");   
    }
    
}

void print_space(int original,int limit){
    for (int row = 0; row < (original - limit); row++){
            printf(" ");
    }
}

void print_star(int limit){
    for (int row = 0; row < limit*2-1; row++){
        printf("*");
    }
}