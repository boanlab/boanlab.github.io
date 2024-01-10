# include <stdio.h>
# include <stdlib.h>
# include <string.h>

typedef struct Node {
    int data;
    struct Node *next;
}Node;

typedef struct Queue {
    Node *front;
    Node *rear;
    int size;
}Queue;

void initQueue(Queue *queue) {
    queue -> front = queue -> rear = NULL;
    queue -> size = 0;
}

int isEmpty(Queue *queue) {
    return queue -> size == 0;
}

void offer(Queue *queue, int data) {
    Node *node = (Node *)malloc(sizeof(Node));
    node -> data = data;
    node -> next = NULL;

    if (isEmpty(queue)) {
        queue -> front = node;
    } else {
        queue -> rear -> next = node;
    }

    queue -> rear = node;
    queue -> size++;
}

int poll(Queue *queue) {
    int result = 0;
    Node *node;

    if (isEmpty(queue)) {
        return result;
    }

    node = queue -> front;
    result = node -> data;
    queue -> front = node -> next;
    free(node);
    queue -> size--;

    return result;
}

int main(void)
{
    int i;
    Queue queue;

    initQueue(&queue);                  
    for (i = 1; i <= 5; i++)            
    {
        offer(&queue, i);
    }
    while (!isEmpty(&queue))           
    {
        printf("%d ", poll(&queue));    // expected output: 1 2 3 4 5
    }
    printf("\n");
    return 0;
}