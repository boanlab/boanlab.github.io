#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
}node;

typedef struct LinkedListBaseStack {
    node *top;
}stack;

void initStack(stack *stack) {
    stack -> top = NULL;
}

int isEmpty(stack *stack) {
    return stack -> top == NULL;
}

void push(stack *stack, int data) {
    node *newNode = (node *)malloc(sizeof(node));
    newNode -> data = data;
    newNode -> next = stack -> top;
    stack -> top = newNode;
}

int pop(stack *stack) {
    if (isEmpty(stack)) {
        return 0;
    }
    
    node *currentNode = stack -> top;
    int result  = currentNode -> data;
    stack -> top = currentNode -> next;
    free(currentNode);

    return result;
}

int main(void)
{
    int i;
    stack stack;

    initStack(&stack);
    for (i = 1; i <= 5; i++)
    {
        push(&stack, i);
    }
    while (!isEmpty(&stack))
    {
        printf("%d ", pop(&stack)); // expected output: 5 4 3 2 1 
    }
    printf("\n");
    return 0;
}