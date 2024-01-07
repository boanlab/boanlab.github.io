class LinkedListQueue:
    class _Node:
        def __init__(self, data, next):
            self._data = data
            self._next = next
        
        def __str__(self):
            return str(self._data)
        
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __iter__(self):
        v = self._front
        while v is not None:
            yield v
            assert isinstance(v._next, object)
            v = v._next

    def __str__(self):
        return " -> ".join(str(v) for v in self)

    
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def offer(self, data):
        node = self._Node(data, None)

        if self.isEmpty():
            self._front = node
        else:
            self._rear._next = node
        
        self._rear = node
        self._size += 1
    
    def poll(self):
        if self.isEmpty():
            return None
        
        if self._size == 1:
            self._rear = None
        
        element = self._front._data
        self._front = self._front._next
        self._size -= 1

        return element
    def peek(self):
        if self.isEmpty():
            return None
        
        return self._front._data

# 테스트
queue = LinkedListQueue()   # 객체 생성
queue.offer('BoanLab')
queue.offer('Apdul')
queue.offer('PeachPotato')
queue.offer('RoyRoy')

print(queue)                # expected output: BoanLab -> Apdul -> PeachPotato -> RoyRoy          