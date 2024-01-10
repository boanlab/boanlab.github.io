package DataStructure;

public class queueArray {

    private int[] queue;

    private int front;
    private int rear;

    public queueArray(int size){ // 큐 생성자

        this.queue = new int[size];
        this.front = -1;
        this.rear = -1;

    }

    void printQueue(){

        for(int i=0; i<queue.length; i++){
            if( i<=front || i>rear)
                System.out.print(" ");
            else
                System.out.print(queue[i] + " ");

        }
        System.out.println();
    }

    boolean isEmpty(){
        if(front == rear){
            return true;
        }
        else{
            return false;
        }
    }

    boolean isFull(){
        if(rear == queue.length-1){
            return true;
        }
        else{
            return false;
        }
    }

    void enqueue(int value){
        if(isFull()){
            System.out.println("큐가 가득찼습니다.");
        }
        else{
            queue[++rear] = value;
        }
    }

    int dequeue(){
        if(isEmpty()){
            System.out.println("큐가 비었습니다.");
            return -1;
        }
        else{
            int result = queue[++front];
            return result;
        }
    }


    public static void main(String[] args) {

        queueArray queue = new queueArray(5);

        queue.enqueue(1);
        queue.printQueue();

        queue.enqueue(2);
        queue.printQueue();

        queue.enqueue(3);
        queue.printQueue();

        queue.enqueue(4);
        queue.printQueue();

        queue.enqueue(5);
        queue.printQueue();

        queue.enqueue(6);

        queue.dequeue();
        queue.printQueue();

    }
}



