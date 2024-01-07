package queue.LinkedListQueue;

public class LinkedListQueueMain {
    public static void main(String[] args) {
        LinkedListQueue queue = new LinkedListQueue();

        queue.offer(522);
        queue.offer("BoanLab");
        queue.offer("Apdul");
        queue.offer("LinkedListQueue");

        while (!queue.isEmpty()) {
            /** expected output
             * 522
             * BoanLab
             * Apdul
             * LinkedListQueue
             */
            System.out.println(queue.poll());
        }
    }
}