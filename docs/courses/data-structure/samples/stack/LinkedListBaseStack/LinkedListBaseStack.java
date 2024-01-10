package LinkedListBaseStack;

import java.util.NoSuchElementException;

public class LinkedListBaseStack {
    private static class Node {
        private Object data;
        private Node next;

        public Node(Object data) {
            this.data = data;
            this.next = null;
        }
    }
    private Node top;

    public LinkedListBaseStack() {
        this.top = null;
    }

    public boolean isEmpty() {
        return top == null;
    }

    public void push(Object data) {
        Node node = new Node(data);
        node.next = top;
        top = node;
    }

    public Object peek() {
        return top.data;
    }

    public Object pop() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        } else {
            Object data = top.data;
            top = top.next;

            return data;
        }
    }
}