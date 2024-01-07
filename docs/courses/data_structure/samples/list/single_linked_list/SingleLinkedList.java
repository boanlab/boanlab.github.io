package singleLinkedList;

import java.util.NoSuchElementException;

public class SingleLinkedList<E> {
    private Node<E> head;
    private Node<E> tail;
    private int size;

    public SingleLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    private Node<E> search(int index) {
        if (index < 0 || index >= size) throw new IndexOutOfBoundsException();

        Node<E> node = head;

        for (int i=0; i < index; i++) node = node.next;

        return node;
    }

    public void addFirst(E value) {
        Node<E> node = new Node<>(value);
        node.next = head;
        head = node;
        size++;

        if (head.next == null) tail = head;
    }

    public void addLast(E value) {
        Node<E> node = new Node<>(value);

        if (size == 0) {
            addFirst(value);
            return;
        }

        tail.next = node;
        tail = node;
        size++;
    }

    public void add(int index, E value) {
        if (index < 0 || index >= size) throw new IndexOutOfBoundsException();

        if (index == 0) {
            addFirst(value);
            return;
        }

        if (index == size) {
            addLast(value);
            return;
        }

        Node<E> node = new Node<>(value);
        Node<E> prevNode = search(index - 1);
        Node<E> nextNode = prevNode.next;

        prevNode.next = null;
        prevNode.next = node;
        node.next = nextNode;
        size++;
    }

    public void removeFirst() {
        Node<E> headNode = head;

        if (headNode == null) throw new NoSuchElementException();

        Node<E> nextNode = head.next;

        head.data = null;
        head.next = null;

        head = nextNode;
        size--;
    }

    public void removeByIndex(int index) {
        if (index < 0 || index >= size) throw new IndexOutOfBoundsException();

        if (index == 0) {
            removeFirst();
            return;
        }

        Node<E> prevNode = search(index - 1);
        Node<E> removeNode = prevNode.next;

        prevNode.next = removeNode.next;

        if (prevNode.next == null) tail = prevNode;

        removeNode.data = null;
        removeNode.next = null;
        size--;
    }

    public void removeByValue(Object value) {
        Node<E> prevNode = head;
        Node<E> node = head;

        for (; node != null; node = node.next) {
            if (value.equals(node.data)) break;
            prevNode = node;
        }

        if (node == null) throw new NullPointerException();

        if (node.equals(head)) {
            removeFirst();
        } else {
            prevNode.next = node.next;

            if (prevNode.next == null) tail = prevNode;

            node.data = null;
            node.next = null;
            size--;
        }
    }

    public E get(int index) {
        return search(index).data;
    }

    public void set(int index, E value) {
        Node<E> node = search(index);
        node.data = null;
        node.data = value;
    }

    public int indexOf(Object value) {
        int index = 0;

        for (Node<E> node = head; node != null; node = node.next) {
            if (value.equals(node.data)) {
                return index;
            }
            index++;
        }

        return -1;
    }

    public boolean contains(Object value) {
        return indexOf(value) >= 0;
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void clear() {
        for (Node<E> node = head; node != null;) {
            Node<E> nextNode = node.next;
            node.data = null;
            node.next = null;
            node = nextNode;
        }
        head = tail = null;
        size = 0;
    }
}

class Node<E> {
    E data;
    Node<E> next;

    Node(E data) {
        this.data = data;
        this.next = null;
    }
}