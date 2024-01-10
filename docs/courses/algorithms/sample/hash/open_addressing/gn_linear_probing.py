class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [[] for i in range(table_size)]
    
    # key 값으로부터 해시 키를 계산하는 메소드
    def get_hash_key(self, key):
        hash_key = 0
        
        for i in key:
            hash_key += ord(i) - ord('a')
        
        # 해시 함수 적용
        hash_key %= self.table_size

        return hash_key
    
    # 삽입
    def add(self, key, value):
        hash_key = self.get_hash_key(key)

        # 해시 충돌이 일어나지 않은 경우
        if not self.hash_table[hash_key]:
            self.hash_table[hash_key] = [key, value]
        else:   # 해시 충돌이 일어난 경우
            next_hash = (hash_key+1) % self.table_size  # 다음 해시 키를 얻는다.
            
            # while문을 통해 해시 테이블에 next_hash에 해당하는 값이 없는 버킷을 찾는다.
            while self.hash_table[next_hash]:
                next_hash = (hash_key+1) % self.table_size
                
                # 해시 테이블을 다 탐색하고, 다시 기존의 해시 키로 돌아온 경우
                if next_hash == hash_key:
                    return
            
            # 새로 찾은 해시 키 next_hash에 key와 value 저장
            self.hash_table[next_hash] = [key, value]

    # 탐색
    def find(self, key):
        hash_key = self.get_hash_key(key)

        if self.hash_table[hash_key][0] == key:
            return self.hash_table[hash_key][1]
        else:
            next_hash = (hash_key+1) % self.table_size

            while self.hash_table[next_hash][0] != key:
                next_hash = (hash_key+1) % self.table_size

                if next_hash == hash_key:
                    return
            
            return self.hash_table[next_hash][1]

# 테스트
test_hash_table = HashTable(10)
test_hash_table.add("abc", 10)
test_hash_table.add("cba", 20)

print(test_hash_table.find("abc"))  # expected output: 10
print(test_hash_table.find("cba"))  # expected output: 20