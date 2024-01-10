def find_string(parent, pattern):
    parent_len = len(parent)    # 검색 대상 문자열 길이
    pattern_len = len(pattern)  # 찾을 문자열(pattern) 
    parent_hash = 0
    pattern_hash = 0
    power = 1
    for i in range(parent_len - pattern_len + 1):
        if i == 0:
            for j in range(pattern_len):
                parent_hash += ord(parent[pattern_len - 1 - j]) * power  # ord : 아스키코드 값 반환
                pattern_hash += ord(pattern[pattern_len - 1 - j]) * power
                if j < pattern_len - 1:
                    power *= 2
        else:
            parent_hash = 2 * (parent_hash - ord(parent[i - 1]) * power) + ord(parent[pattern_len - 1 + i])

        if parent_hash == pattern_hash:
            found = True
            for j in range(pattern_len):
                if parent[i + j] != pattern[j]:
                    found = False
                    break
            if found:
                print(f'{i + 1}번째에서 발견')

                
if __name__ == "__main__":
    parent = "ababacabacaabacaaba"
    pattern = "abacaaba"
    find_string(parent, pattern)
