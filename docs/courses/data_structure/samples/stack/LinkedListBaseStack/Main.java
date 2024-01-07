package LinkedListBaseStack;

public class Main {
    public static void main(String[] args) {
        LinkedListBaseStack stack = new LinkedListBaseStack();

        stack.push(522);
        stack.push("BoanLab");
        stack.push("Apdul");
        stack.push("LinkedListBaseStack");

        while(!stack.isEmpty()){
            /** expected output
             *  LinkedListBaseStack
             *  Apdul
             *  BoanLab
             *  522
             */
            System.out.println(stack.pop());
        }
    }
}