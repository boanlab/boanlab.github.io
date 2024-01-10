# Node 클래스
class Node:
    def __init__(self, item):
        self.item = item    # Node가 갖는 값을 저장하는 변수 item
        self.left = None    # left child Node를 가리키는 변수 left
        self.right = None   # right child Node를 가리키는 변수 right

# 이진탐색트리 클래스
# 재귀를 이용한 이진탐색트리
class BinarySearchTree:
    def __init__(self, root):
        self.root = root
    
    # 노드 삽입
    def insert(self, data):
        self.root = self._insert_data(self.root, data)
        return self.root is not None

    def _insert_data(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data<=node.item:
                node.left = self._insert_data(node.left, data)
            else:
                node.right = self._insert_data(node.right, data)
        return node
    
    # 노드 탐색
    def find(self, key):
        return self._find_data(self.root, key)
    
    def _find_data(self, root, key):
        if root is None or root.item == key:
            return root is not None
        elif key < root.item:
            return self._find_data(root.left, key)
        else:
            return self._find_data(root.right, key)

    # 노드 삭제
    def delete(self, key):
        self.root, deleted = self._deleted_data(self.root, key)
        return deleted
    
    def _deleted_data(self, node, key):
        deleted = False
        if node is None:
            return node, deleted
        
        # 해당 노드가 삭제할 노드일 경우
        if key == node.item:
            deleted = True
            
            # 삭제할 노드의 자식 노드가 두 개인 경우
            if node.left and node.right:    
                parent, child = node, node.right
                
                # 오른쪽 서브 트리의 가장 왼쪽 리프 노드에 있는 노드를 찾아 교체 
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # 자식 노드 하나일 경우 해당 노드와 교체
            elif node.left or node.right:
                node = node.left or node.right
            # 자식 노드가 없는 경우 그냥 삭제
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._deleted_data(node.left, key)
        else:
            node.right, deleted = self._deleted_data(node.right, key)
        return node, deleted

    # 전위순회 메소드 preorder
    def preorder(self):
        def _preorder(root):
            if root is None:
                pass
            else:
                print(root.item)
                _preorder(root.left)
                _preorder(root.right)
        
        _preorder(self.root)
        
# 테스트
arr = [7, 3, 5, 22, 10, 13, 17, 75, 45, 9]
root = Node(30)
binary_search_tree = BinarySearchTree(root)

for i in arr:
    binary_search_tree.insert(i)

'''
expected output:
30
7
3
5
22
10
9
13
17
75
45
'''
binary_search_tree.preorder() 



                

    