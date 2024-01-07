#include <stdio.h>
#include <stdlib.h>

int *stack;
int top = -1;

int *InputData(void){
    int *data;
    int num;
    
    printf("Insert number you want to push in stack:");
    
    scanf("%d", &num);
    
    printf("%d\n", num);
    
    data = (int *)malloc(sizeof(int) * ((num)+1)); // malloc : 할당된 메모리의 '주소'가 void* 형으로 리턴된다.
    
    printf("Insert data you want to push in stack\n");
    
    for(int i = 0; i < (num+1); i++){
        if(i == 0){
            printf("data[%d] = the number of data array\n", i);
            data[0] = num;
        }
        else{
            printf("data[%d] = ",i);
            scanf("%d", &data[i]);
        }
    }
    
    printf("\n");
    
    for(int i = 0; i < (num+1); i++)
        printf("data[%d] = %d\n", i, data[i]);
    
    return data;
}

void push(int *val){
    int num;
    num = val[0];
    
    int *stack_temp;
    stack_temp = stack;
    
    free(stack);
    stack = (int *)malloc(sizeof(int) * (num + (top+1)));
    
    puts("\nTramsplant starts");
    
    if(top == -1){
        printf("Stack is empty.\n");
    }
    else{
        for(int i = 0; i <= top; i++){
            stack[i] = stack_temp[i];
            printf("stack[%d] = %d\n", i, stack[i]);
        }
    }
    puts("Tramsplant is complete.\n");
    for(int i = 1; i <= num; i++){
        stack[++top] = val[i];
    }
}

void pop(unsigned int num){
    if(top < 0){
        printf("Stack is empty.\n");
    }
    else{
        int poped_stack[num];   
        
        for(int i = 0; i < num; i++){
            if(top < 0){
                printf("Stack is empty.\n");
                break;
            }
            poped_stack[i] = stack[top--];
            printf("poped_stack[%d] = %d\n", i, poped_stack[i]);
        }
    }
}

void PrintStack(void){
    puts("\nPrinting stack starts.");
    
    if(top < 0){
        printf("Stack is empty.\n");
    }
    else{
        int num;
        num = top;
    
        while(num != -1){
            printf("stack[%d] = %d\n", num, stack[num]);
            num--;
        }
    }  
    puts("Printing stack is complete.\n");
}
 
int main(void){    
    push(InputData());    
    PrintStack();    
    push(InputData());    
    PrintStack();  
    pop(3);
    pop(4);
    pop(3);
    return 0;
}