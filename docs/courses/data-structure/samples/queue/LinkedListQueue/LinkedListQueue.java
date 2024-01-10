package queue.LinkedListQueue;

public class LinkedListQueue<E> {
    private Node<E> front;
    private Node<E> rear;
    private int size;

    public LinkedListQueue() {
        this.front = null;
        this.rear = null;
        this.size = 0;
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void offer(E value) {
        Node<E> node = new Node<>(value);

        if (isEmpty()) {
            front = node;
        } else {
            rear.next = node;
        }

        rear = node;
        size++;
    }

    public E poll() {
        if (isEmpty()) return null;

        E element = front.data;
        Node<E> nextNode = front.next;

        front.data = null;
        front.next = null;

        front = nextNode;
        size--;

        return element;
    }

    public E peek() {
        if (isEmpty()) return null;

        return front.data;
    }
}

class Node<E> {
    E data;
    Node<E> next;

    public Node(final E data) {
        this.data = data;
        this.next = null;
    }
}