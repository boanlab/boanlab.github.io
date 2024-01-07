package DataStructure.queue;

public class CircularQueue {


    private int[] queue;

    private int front;
    private int rear;


    public CircularQueue(int size){ // 큐 생성자

        this.queue = new int[size];
        this.front = 0;
        this.rear = 0;


    }

    void printQueue(){  // front + 1 부터 rear -1 까지 읽어야 한다. (순환 인 것을 유의)

        if(isEmpty()){
            System.out.println("큐가 비었습니다.");
        }
        else{

            int i = front;

            do{
                i = (i+1) % queue.length;
                System.out.print(queue[i] + " ");

                if(i==rear)
                    break;

            }while(i!=rear);

            System.out.println();
        }
    }

    boolean isEmpty(){
        if(front == rear)
            return true;

        else
            return false;
    }

    boolean isFull(){
        if(front == (rear+1) % queue.length)
            return true;
        else
            return false;
    }


    void enqueue(int value){

        if(isFull()){
            System.out.println("큐가 가득찼습니다.");
        }
        else{

            rear = (rear+1) % queue.length; // rear 값을 1 증가 시키고(모듈러 연산 포함)
            queue[rear] = value; // 값을 인큐


        }
    }

    int dequeue(){
        if(isEmpty()){
            System.out.println("큐가 비었습니다.");
            return -1;
        }
        else{
            front = (front+1) % queue.length;
            int result = queue[front];
            return result;
        }
    }



    public static void main(String[] args) {


        // 테스트!

        CircularQueue cirQueue = new CircularQueue(5);

        cirQueue.enqueue(1);
        cirQueue.printQueue();          // 1

        cirQueue.enqueue(2);
        cirQueue.printQueue();          // 1 2

        cirQueue.enqueue(3);
        cirQueue.printQueue();          // 1 2 3

        cirQueue.dequeue();
        cirQueue.printQueue();          //  2 3

        cirQueue.dequeue();
        cirQueue.printQueue();          //  3

        cirQueue.dequeue();
        cirQueue.printQueue();          // empty

    }
}