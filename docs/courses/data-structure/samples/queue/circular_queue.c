
#include <stdio.h>

#define MAX_QUEUE_SIZE 5  // 큐(배열)의 최대 길이 설정


typedef struct {

    int front;
    int rear;
    int data[MAX_QUEUE_SIZE];

}queue_type;


void init(queue_type *q);
void print_queue(queue_type *q);

int is_empty(queue_type  *q);
int is_full(queue_type *q);

void enqueue(queue_type *q, int value);
int dequeue(queue_type *q);


int main(void){


    queue_type cir_queue;

    init(&cir_queue);

    enqueue(&cir_queue,1);  // 1
    print_queue(&cir_queue);
    
    enqueue(&cir_queue,2);  // 1 2
    print_queue(&cir_queue);

    enqueue(&cir_queue,3); // 1 2 3
    print_queue(&cir_queue);

    dequeue(&cir_queue); // 2 3
    print_queue(&cir_queue);

    dequeue(&cir_queue); // 3
    print_queue(&cir_queue);

    dequeue(&cir_queue); // empty
    print_queue(&cir_queue); // 큐가 비었습니다.
}


void init(queue_type *q){

    q->front = 0;
    q->rear = 0;  // 각각 0으로 초기화
}


void print_queue(queue_type *q){

    if(is_empty(q)){ // 큐가 비었는 지 체크
        printf("큐가 비었습니다.");
    }

    else{

        int i = q->front;

        do{
            i = (i + 1) % MAX_QUEUE_SIZE; // 
            printf("%d ", q->data[i]);
            if(i==q->rear)
                break;
        
        }while(i!=q->front);

        printf("\n");
    }
}

int is_empty(queue_type *q){

    return q->front == q->rear;
}

int is_full(queue_type *q){

    return q->front == ((q->rear+1) % MAX_QUEUE_SIZE);
}

void enqueue(queue_type *q, int value){
    
    if(is_full(q)){
        printf("큐가 가득 찼습니다.");
    }
    else{
        q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
        q->data[q->rear] = value;
    }
    
}

int dequeue(queue_type *q){

    if(is_empty(q)){
        printf("큐가 비었습니다.");
    }
    else{ 
        q->front = (q->front+1) % MAX_QUEUE_SIZE;
        int result = q->data[q->front];
        return result;
    }
}