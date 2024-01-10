# 아직 제 스타일대로 변경은 하지 못했습니다. 참고 바랍니다.

class Node():
    def __init__(self, data):
        self.data = data
        self.parent = self.left = self.right = None
        self.color = 'Red' # 신규 삽입되는 노드는 항상 빨강
          
class RedBlackTree:
    
    # 조부모 노드 찾기
    def find_grandparent_node(self,node):
        if (node != None and node.parent != None):
            return node.parent.parent
        else:
            return None
    
    # 삼촌 노드 찾기
    def find_uncle_node(self,node):
        grandparent_node = self.find_grandparent_node(node)
        if grandparent_node == None:
            return None
    
        if node.parent == grandparent_node.left:
            return grandparent_node.right
        else:
            return grandparent_node.left
        
    # case1. 루트 노드는 항상 블랙  
    def insert_case1(self,node):
        if node.parent == None:
            node.color = 'Black'
        else:
            self.insert_case2(node)
        
    # case2. 부모 노드가 블랙이면 회전, 색변환등 수행 필요 x, 하지만 빨강색이라면 case3 수행
    def insert_case2(self,node):
        if node.parent.color == 'Black':
            return
        else:
            self.insert_case3(node)
    
    # case3. 부모노드, 삼촌노드 모두 빨강이라면 색변환 수행, 아닐경우 case4로 이동
    def insert_case3(self,node):
        uncle = self.find_uncle_node(node)
    
        if (uncle != None and uncle.color == 'Red'):
            node.parent.color = 'Black'
            uncle.color = 'Black'
            grandparent = self.find_grandparent_node(node)
            grandparent.color = 'Red'
            self.insert_case1(grandparent)
        else:
            self.insert_case4(node)
    
    
    # case4,5 회전 수행
    def insert_case4(self,node):
        
        grandparent = self.find_grandparent_node(node)
    
        if(node == node.parent.right and node.parent == grandparent.left):
            self.rotate_left(node.parent)
            node = node.left
        elif (node == node.parent.left and node.parent == grandparent.right):
            self.rotate_right(node.parent)
            node = node.right
    
        self.insert_case5(node)
    
    def rotate_left(self,node):
        c = node.right
        p = node.parent
    
        if (c.left != None):
            c.left.parent = node
    
        node.right = c.left
        node.parent = c
        c.left = node
        c.parent = p
        
        if c.parent == None:
            self.root = c
    
        if (p != None):
            if (p.left == node):
                p.left = c
            else:
                p.right = c

    def rotate_right(self,node):
        c = node.left
        p = node.parent
    
        if (c.right != None):
            c.right.parent = node
    
        node.left = c.right
        node.parent = c
        c.right = node
        c.parent = p
        
        if c.parent == None:
            self.root = c
            
        if (p != None):
            if (p.right == node):
                p.right = c
            else:
                p.left = c
     
    def insert_case5(self,node):
        grandparent = self.find_grandparent_node(node)
    
        node.parent.color = 'Black'
        grandparent.color = 'Red'

        if (node == node.parent.left):
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

            
    def __init__(self):
        self.root = None
        self.inserted_node = None
	
    # 삽입
    def insert(self, data, parent_node):
        self.root = self.insert_value(self.root, data, parent_node)
        self.insert_case1(self.inserted_node)
        return 
    
    def insert_value(self, node, data, parent_node):
        if node is None:
            node = Node(data)
            node.parent = parent_node
            self.inserted_node = node
        else:
            if data <= node.data:
                node.left = self.insert_value(node.left,data,node)
            else:
                node.right = self.insert_value(node.right,data,node)
        return node
    
    # 탐색
    def find(self,search_key):
        return self.find_value(self.root, search_key)
    
    def find_value(self, root, search_key):
        if root is None or root.data == search_key:
            return root 
        elif search_key > root.data:
            return self.find_value(root.right, search_key)
        else:
            return self.find_value(root.left, search_key)      




rbt = RedBlackTree()

a = [2, 1, 8, 9, 7, 3, 6, 4, 5]
    
for x in a:
    rbt.insert(x,None)
    

# 레드블랙트리 key, 부모, 색상 출력
def check(node):
    if not node.left  == None : check(node.left)
    if node.parent != None:
        print('key: ', node.data, 'parents: ', node.parent.data, 'color: ', node.color, end = '\n')
    else:
        print('key: ', node.data, 'parents: ', node.parent, 'color: ', node.color, end = '\n')
    if not node.right == None : check(node.right)

check(rbt.root)
