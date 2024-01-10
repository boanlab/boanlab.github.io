class PriorityQueue:
    def __init__(self):
        self.items = [None]
    
    # 우선순위 큐가 생성되면 items에 None을 원소로 포함하기 때문에 길이는 (items-1)
    def __len__(self):
        return len(self.items) - 1
    
    # 우선순위 큐의 값을 확인하기 위한 repr 메소드
    def __repr__(self):
        return ' '.join(map(str, self.items[1:]))

    # 삽입 후, 루트 노드까지 거슬러 올라가며 최대 합을 구하기 위한 메소드
    def _percolate_up(self):
        length = len(self)
        parent = length // 2

        while length > 1:
            if self.items[parent] > self.items[length]:
                self.items[parent], self.items[length] = self.items[length], self.items[parent]
            
            length = parent
            parent //= 2
    
    # 삭제 후, 리프 노드까지 내려가면서 최대 합을 구성하기 위한 메소드
    def _percolate_down(self, idx=1):
        left, right = idx << 1, idx << 1|1
        minimum = idx

        if left < len(self) and self.items[left] < self.items[minimum]:
            minimum = left
        if right < len(self) and self.items[right] < self.items[minimum]:
            minimum = right
        if minimum != idx:
            self.items[idx], self.items[minimum] = self.items[minimum], self.items[idx]
            self._percolate_down(minimum)

    # 삽입
    def heap_push(self, item):
        self.items.append(item)
        self._percolate_up()
    
    # 삭제
    def heap_pop(self):
        result = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down()
        return result

# 테스트
priority_queue = PriorityQueue()
input_array = [4, 10, 24, 0, 522, 2, 73, 39, 6, 12]

for num in input_array:
    priority_queue.heap_push(num)

print(priority_queue)               # expected output: 0 4 2 6 12 24 73 39 10 522
priority_queue.heap_push(9)
print(priority_queue)               # expected output: 0 4 2 6 9 24 73 39 10 522 12
print(priority_queue.heap_pop())    # expected output: 0
print(priority_queue)               # expected output: 2 4 12 6 9 24 73 39 10 522

