class Node:
    def __init__(self, value=None, link=None):
        self.value = value
        self.next = link

    def __str__(self):
        return str(self.value)
        


class LinkedListBaseStack:
    def __init__(self):
        self.head = None

    def __iter__(self):
        v = self.head
        while v is not None:
            yield v
            assert isinstance(v.next, object)
            v = v.next
    
    def __str__(self):
        return " -> ".join(str(v) for v in self)
    
    def isEmpty(self):
        if self.head:
            return False
        return True
    
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.isEmpty():
            return -1
        data = self.head.value
        self.head = self.head.next

        return data
    
    def peek(self):
        if self.isEmpty():
            return -1

        return self.head.value

# 테스트
stack = LinkedListBaseStack()

stack.push(522)
stack.push("BoanLab")
stack.push("Apdul")
stack.push("LinkedListBaseStack")

'''
expected output
LinkedListBaseStack
Apdul
BoanLab
522
'''
while not stack.isEmpty():
    print(stack.pop())