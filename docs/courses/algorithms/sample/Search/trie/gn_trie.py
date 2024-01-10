class Node:
    def __init__(self, key, data=None):
        self.key = key      # 해당 문자
        self.data = data    # 문자열이 끝나는 위치를 알려주는 역할, 해당 노드에서 끝나는 문자열이 없을 경우 None
        self.children = {}  # 자식 노들을 해당 문자를 키로 갖는 딕셔너리로 저장할 children 필드

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    # 삽입
    def insert(self, string):
        current_node = self.head

        
        # 반복문을 이용해 string의 문자별로 노드가 존재하는지 확인
        for char in string:
            # string의 해당 문자에 대한 노드가 없는 경우
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            
            # 해당 문자의 노드로 current_node 이동
            current_node = current_node.children[char]
        
        # string이 끝난 지점의 노드의 ㅇdata 값에 해당 문자열을 입력
        current_node.data = string
    
    # 검색
    def search(self, string):
        current_node = self.head

        # 반복문을 이용해 string의 문자별로 노드가 존재하는지 확인
        for char in string:
            # string의 해당 문자에 대한 노드가 있는 경우
            if char in current_node.children:
                current_node = current_node.children[char]
            else:   # 없는 경우 해당 노드가 없다는 결과 return
                return False
        
        if current_node.data != None:
            return True
    
    # 사전 검색
    def start_with(self, prefix):
        current_node = self.head
        words = []

        # 반복문을 이용해 prefix의 문자별로 노드가 존재하는지 확인
        for char in prefix:
            # prefix의 해당 문자에 대한 노드가 있는 경우 
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None
        
        current_node = [current_node]
        next_node = []

        # while문을 이용해 prefix로 시작하는 노드를 words에 추가
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break
        
        return words


# 테스트
trie = Trie()
word_list = ["frodo", "front", "firefox", "fire"]

for word in word_list:
    trie.insert(word)

print(trie.search("frodo"))     # expected output: True
print(trie.search("friend"))    # expected output: False
print(trie.search("fire"))      # expected output: True
print(trie.start_with("fro"))   # expected output: ['frodo', 'front']
print(trie.start_with("fir"))   # expected output: ['fire', 'firefox']
print(trie.start_with("boan"))  # expected output: None
print(trie.start_with("f"))     # expected output: ['fire', 'frodo', 'front', 'firefox']



