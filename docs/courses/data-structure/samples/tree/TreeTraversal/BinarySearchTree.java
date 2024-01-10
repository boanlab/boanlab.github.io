package TreeTraversal;

// Node 클래스
class Node {
    int item;   // Node가 갖는 값을 저장하는 변수 item
    Node left;  // left child Node를 가리키는 변수 left
    Node right; // right child Node를 가리키는 변수 right

    // Node 클래스 생성자
    Node(int value) {
        this.item = value;
        this.left = null;
        this.right = null;
    }

    /**
     * Node 클래스 필드별 getter, setter 메소드
     * 
     */
    public int getItem() {
        return item;
    }

    public Node getLeft() {
        return left;
    }

    public Node getRight() {
        return right;
    }

    public void setItem(int value) {
        this.item = value;
    }

    public void setLeft(Node left) {
        this.left = left;
    }

    public void setRight(Node right) {
        this.right = right;
    }
}

// 이진탐색트리 클래스
public class BinarySearchTree {
    private Node root;  // root Node

    // 생성자
    public BinarySearchTree() {
        this.root = null;
    }

    // 노드 삽입
    public void insert(int value) {
        Node newNode = new Node(value);
        Node currentNode = root;
        Node parentNode = null;

        if (root == null) {
            root = newNode;
            return;
        }

        while (true) {
            parentNode = currentNode;

            if (value < currentNode.getItem()) {    // 현재 노드보다 value가 작은 경우
                currentNode = currentNode.getLeft();

                if (currentNode == null) {
                    parentNode.setLeft(newNode);
                    break;
                }
            } else {                                // 현재 노드보다 value가 큰 경우
                currentNode = currentNode.getRight();
                if (currentNode == null) {
                    parentNode.setRight(newNode);
                    break;
                }
            }
        }
    }

    // 노드 삭제
    public boolean remove(int key) {
        Node currentNode = root;
        Node parentNode = root;
        boolean isLeftChild = false;

        while (currentNode.getItem() != key) {  // key에 해당하는 노드로 이동하기 위한 while문
            parentNode = currentNode;

            if (key < currentNode.getItem()) {
                isLeftChild = true;
                currentNode = currentNode.getLeft();
            } else {
                isLeftChild = false;
                currentNode = currentNode.getRight();
            }

            if (currentNode == null) {
                return false;
            }
        }

        if (currentNode.getLeft() == null && currentNode.getRight() == null) {  // 삭제할 노드의 child node가 없는 경우
            if (currentNode == root) {  // 해당 노드가 root node일 경우
                root = null;
            }

            if (isLeftChild) {  // 삭제할 노드가 parent node의 left child일 경우
                parentNode.setLeft(null);
            } else {            // 삭제할 노드가 parent node의 right child일 경우
                parentNode.setRight(null);
            }
        } else if (currentNode.getRight() == null) {    // 삭제할 노드의 child node가 right child 하나일 경우
            parentNode.setLeft(currentNode.getLeft());
        } else if (currentNode.getLeft() == null) {     // 삭제할 노드의 child node가 left child 하나일 경우
            parentNode.setRight(currentNode.getRight());
        } else {                                        // 삭제할 노드의 child node가 양 쪽 다 있는 경우
            Node leaf = getLeaf(currentNode);

            if (currentNode == root) {
                root = leaf;
            } else if (isLeftChild) {
                parentNode.setLeft(leaf);
            } else {
                parentNode.setLeft(currentNode.getLeft());
            }
            leaf.setLeft(currentNode.getLeft());
        }
        return false;
    }

    // 노드 삭제 후 삭제 한 자리에 들어갈 노드를 찾기 위한 메소드
    Node getLeaf(Node deletedNode) {
        Node leaf = null;
        Node leafParent = null;
        Node currentNode = deletedNode.getRight();

        while (currentNode != null) {
            leafParent = leaf;
            leaf = leafParent;
            currentNode = currentNode.getLeft();
        }

        if (leaf != deletedNode.getRight()) {
            leafParent.setLeft(leaf.getRight());
            leaf.setRight(deletedNode.getRight());
        }
        return leaf;
    }

    // 전위순회 메소드 preorder
    public void preorder() {
        preorder(this.root);
    }

    public void preorder(Node node) {
        if (node != null) {
            System.out.print(node.getItem() + " ");
            preorder(node.getLeft());
            preorder(node.getRight());
        }
    }

    // 테스트
    public static void main(String[] args) {
        BinarySearchTree binarySearchTree = new BinarySearchTree();
        int[] array = {7, 3, 5, 22, 10, 13, 17, 75, 45, 9};

        for (int i=0; i<array.length; i++) {
            binarySearchTree.insert(array[i]);
        }

        binarySearchTree.preorder();    // expected output: 7 3 5 22 10 9 13 17 75 45 
    }
}