#include <stdio.h>

#define MAX_QUEUE_SIZE 5  // 큐(배열)의 최대 길이 설정


typedef struct{
    int front;
    int rear;
    int data[MAX_QUEUE_SIZE]; // int형 배열 큐 선언
}queue_type;


void init(queue_type *q); // 큐의 초기상태 설정
int is_empty(queue_type *q);
int is_full(queue_type *q);
void enqueue(queue_type *q, int value);
void print_queue(queue_type *q);
int dequeue(queue_type *q);


int main(void){

    queue_type queue;

    init(&queue); // 큐 생성

    enqueue(&queue,1);
    print_queue(&queue);

    enqueue(&queue,2);
    print_queue(&queue);

    enqueue(&queue,3);
    print_queue(&queue);

    enqueue(&queue,4);
    print_queue(&queue);

    enqueue(&queue,5);
    print_queue(&queue);

    enqueue(&queue,6); // full , 인큐 실행 불가


    dequeue(&queue);
    print_queue(&queue);

    
}


void init(queue_type *q){
    q->front = -1;
    q->rear = -1;
}

void print_queue(queue_type *q){
    
    int i;
   
    for(i=0; i<MAX_QUEUE_SIZE; i++){
        if( i<= q->front || i> q->rear)
            printf(" ");
        else
            printf("%d ",  q->data[i]);
    }
    printf("\n");
}

int is_empty(queue_type *q){
    return q->front == q->rear;
}


int is_full(queue_type *q){
    return q->rear == MAX_QUEUE_SIZE -1;
}

void enqueue(queue_type *q, int value){

    if(is_full(q)){
        printf("큐가 가득찼습니다.\n");
        return;
    }
    
    q->data[++(q->rear)] = value;
    
}

int dequeue(queue_type *q){

    if(is_empty(q)){
        printf("큐가 비었습니다.\n");
        return -1;
    }

    int result = q->data[++(q->front)];
    return result;
}