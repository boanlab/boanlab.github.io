
//Node class
class Node {
   int value;
   Node leftChild;
   Node rightChild;
   
   //생성자
   public Node(int value) {
      this.value = value;
      this.leftChild = null;
      this.rightChild = null;
   }

}


//BinarySearchTree class
class BinaryTree{
   Node rootNode = null;
   
   //노드 삽입
   public void insertNode(int element) {
      //아무 노드도 없을 때
      if ( rootNode == null) {
         rootNode = new Node(element);
      }
      else {
         Node head = rootNode;
         Node currentNode;
         
         while ( true ) {
            currentNode = head;
            
            //루트노드보다 작은 경우 왼쪽으로 탐색
            if ( head.value > element) {
               head = head.leftChild;
               
               //왼쪽 자식노드가 없으면, 그 위치에 삽입할 노드를 추가한다.
               if ( head == null ) {
                  currentNode.leftChild = new Node(element);
                  break;
               }
            }else {
               //루트노드보다 큰 경우 오른쪽으로 탐색
               head = head.rightChild;
               
               //오른쪽 자식노드가 없으면, 그 위치에 삽입할 노드를 추가한다.
               if ( head == null ) {
                  currentNode.rightChild = new Node(element);
                  break;
            }
         }
      }
   }
}

//특정 노드 삭제
public boolean removeNode(int element) {
   //삭제할 노드를 먼저 루트노드로 놓는다.
   Node removeNode = rootNode;
   //삭제할 노드의 부모노드 정의
   Node parentOfRemoveNode = null;
   
   //삭제할 노드와 루트노드가 같지 않으면
   while(removeNode.value != element) {
      //삭제할 노드의 부모노드는 루트노드
      parentOfRemoveNode = removeNode;
      
      //현재까지 removeNode == parentOfRemoveNode == rootNode
      //삭제할 노드가 현재노드보다 작으면 왼쪽으로 탐색
      if ( removeNode.value > element) {
         removeNode = removeNode.leftChild;
      }else {
         removeNode = removeNode.rightChild;
      }
      
      //Leaf Node일 경우 탐색 실패
      if ( removeNode == null) {
         
         System.out.println("찾기 실패");
         return false;
      }
      
   }
   
   //자식 노드가 모두 없을 떄
   if ( removeNode.leftChild == null && removeNode.rightChild == null ) {
      //removeNode가 루트일때
      if ( removeNode == rootNode ) {
         rootNode = null;
         //삭제할 노드가 삭제할 부모노드의 오른쪽 자식일 때 삭제
      }else if ( removeNode == parentOfRemoveNode.rightChild ) {
         parentOfRemoveNode.rightChild = null;
         //삭제할 노드가 삭제할 부모노드의 왼쪽 자식일 때 삭제
      }else {
         parentOfRemoveNode.leftChild = null;
      }
   }
   //오른쪽 자식만 있을 경우
   else if ( removeNode.leftChild == null ) {
      //removeNode가 루트일때
      if ( removeNode == rootNode ) {
         //루트노드를 오른쪽 자식으로 대체
         rootNode = removeNode.rightChild;
         //삭제할 노드가 부모노드의 오른쪽 자식일 경우
      }else if ( removeNode == parentOfRemoveNode.rightChild) {
         //현재 삭제할 노드 위치에 삭제할 노드의 오른쪽 자식을 올린다. ( 오른쪽 자식만 있으니깐)
         parentOfRemoveNode.rightChild = removeNode.rightChild;
      } else {
         parentOfRemoveNode.leftChild = removeNode.rightChild;
      }
   }
   
   //왼쪽 자식만 있는 경우
   else if ( removeNode.rightChild == null ) {
      //removeNode가 루트일 때
      if ( removeNode == rootNode ) {
         //루트노드를 왼쪽 자식으로 대체
         rootNode = removeNode.leftChild;
         //삭제할 노드가 부모노드의 오른쪽 자식일 경우
      } else if ( removeNode == parentOfRemoveNode.rightChild) {
         //현재 삭제할 노드 위치에 삭제할 노드의 왼쪽 자식을 올린다. ( 왼쪽 자식만 있으니깐)
         parentOfRemoveNode.rightChild = removeNode.leftChild;
      } else {
         parentOfRemoveNode.leftChild = removeNode.leftChild;
      }
   }
   //자식이 둘다 있는 경우
   //오른쪽 서브트리에서 최소값의 노드를 올린다.
   else {
      //삭제할 노드의 자식노드 중 대체될 노드를 지정하고 그 부모를 지정
      Node parentOfReplaceNode = removeNode;
      //삭제할 노드의 오른쪽 서브트리 탐색을 위해 대체될 노드 지정
      Node replaceNode = parentOfReplaceNode.rightChild;
      
      //replace노드의 왼쪽자식이 있으면
      while ( replaceNode.leftChild != null ) {
         //replace 노드를 그 왼쪽 자식으로 대체
         parentOfReplaceNode = replaceNode;
         replaceNode = replaceNode.leftChild;
      }
      
      if ( replaceNode != removeNode.rightChild ) {
         //가장 작은 값을 선택하기 때문에 replaceNode 노드의 왼쪽은 빈자식이 된다.
         parentOfReplaceNode.leftChild = replaceNode.rightChild;
         // replace할 노드의 오른쪽 자식이 삭제할 노드의 오른쪽 자식으로 오게한다. ( replace할 Node를 removeNode로 옮긴다고 생각)
         replaceNode.rightChild = removeNode.rightChild;
      }
      
      //삭제할 노드가 루트이면
      if ( removeNode == rootNode ) {
         rootNode = replaceNode;
      } else if ( removeNode == parentOfRemoveNode.rightChild) {
         //removeNode가 오른쪽 자식이면 그 자리에 replaceNode
         parentOfRemoveNode.rightChild = replaceNode;
      } else {
         parentOfRemoveNode.leftChild = replaceNode;
      }
      //삭제 노드의 왼쪽 자식을 replaceNode와 연결
      replaceNode.leftChild = removeNode.leftChild;
   }
      return true;
   }

   //중위 순회
   public void inorderTree ( Node root, int depth ) {
      if ( root != null ) {
         inorderTree(root.leftChild, depth + 1);
         for ( int i = 0; i< depth; i++) {
            System.out.print("ㄴ");
            
         }
         System.out.println(root.value);
         
         inorderTree(root.rightChild, depth +1);
      }
   }
}
public class Main {
   
   public static void main(String[] args) {
      
      BinaryTree tree = new BinaryTree();
      tree.insertNode(5);
      tree.insertNode(8);
      tree.insertNode(7);
      tree.insertNode(10);
      tree.insertNode(9);
      tree.insertNode(11);
      
      if ( tree.removeNode(10)) {
         System.out.println("노드 삭제");
      }
      
      System.out.println("rootNode is "+tree.rootNode.value);  //5
      
      tree.inorderTree(tree.rootNode,0);	
      

   }

}