class SingleLinkedList:
    class _Node:
        def __init__(self, value=None, link=None):    # 노드 생성자
            self._value = value             # 저장된 데이터           
            self._next = link               # 다음 노드 래퍼런스
        
        def __str__(self):
            return str(self._value)
    
    def __init__(self):
        self._head = None                   # 첫 생성 시 내부에 노드가 없음
    
    def __iter__(self):
        v = self._head
        while v is not None:
            yield v
            assert isinstance(v._next, object)
            v = v._next

    def __str__(self):
        return " -> ".join(str(v) for v in self)

    # 삽입 - 첫번째
    def addFirst(self, value):
        self._head = self._Node(value, self._head)
    
    # 삽입 - node가 가리키는 노드 다음에 새 노드 삽입
    def addAfter(self, value, node):
        node._next = SingleLinkedList._Node(value, node._next)  # 새 노드가 node 다음 노드로 들어감

    # 삭제 - 첫번째
    def deleteFirst(self):
        if self._head is None:
            print("Any Node Exist in List")
            return None
        node = self._head
        self._head = self._head._next
        return node
    
    # 삭제 - node가 가리키는 다음 노드 삭제
    def deleteAfter(self, node):
        if self._head is None:
            print("Any Node Exist in List")
            return None
        tempNode = node._next
        node._next = tempNode._next

    # 탐색
    def search(self, value):
        if self._head is None:
            print("Any Node Exist in List")
            return None
        for v in self:
            if v._value == value:
                return v
        return None   
    
    # 인덱스에 해당하는 값 출력
    def nodeAt(self, index):
        if not isinstance(index, int):
            raise TypeError('Invalid index type')

        if not self._head:
            raise IndexError("Index out of range")
        
        current = self._head
        for i in range(index):
            current = current._next
        return current

# 테스트
s = SingleLinkedList()      # 객체 생성
s.addFirst('BoanLab')
s.addFirst('Apdul')
s.addAfter('PeachPotato', s._head._next)
s.addFirst('RoyRoy')

print(s)                    # expected output: RoyRoy -> Apdul -> BoanLab -> PeachPotato
print(s.search('Apdul'))    # expected output: Apdul
print(s.nodeAt(2))          # expected output: BoanLab     

s.deleteFirst()
s.deleteAfter(s._head)      

print(s)                    # expected output: Apdul -> PeachPotato