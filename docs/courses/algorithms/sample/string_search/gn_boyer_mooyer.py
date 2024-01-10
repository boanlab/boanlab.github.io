# 보이어 무어 알고리즘 
def boyer_moore(pattern, text):
    pattern_length = len(pattern)   # 패턴 문자열의 길이
    text_length = len(text)         # 텍스트 문자열의 길이
    i = 0

    # while문을 이용해 텍스트 내의 패턴과 매칭될 때까지 skip 과정을 반복한다.
    # 최대 반복 횟수는 (텍스트 길이-패턴 길이)만큼한다.
    while (i<=text_length-pattern_length):
        # 패턴 문자열의 인덱스를 받을 idx로 보이어 무어 알고리즘은 뒤에서부터 접근하므로 (패턴 길이-1)로 선언 및 초기화
        idx = pattern_length -1 

        while idx >= 0:
            if pattern[idx] != text[i+idx]:                         # 패턴의 글자와 텍스트의 글자가 다른 경우
                move = get_skip(pattern, text[i+pattern_length-1])  # 해당 불일치 문자의 skip 칸을 알기 위해 get_skip() 호출
                break
            
            idx -= 1

       
        if idx == -1:   # 문자열 탐색에 성공한 경우
            return True
        else:           # 문자열 탐색에 실패한 경우  
            i += move   # move만큼 skip

    return False    

# skip 테이블의 역할을 하는 메소드 get_skip         
def get_skip(pattern, char):
    # for문을 이용해 불일치 문자 char가 패턴 문자열에 있는지 검사
    # 패턴의 마지막 문자와 불일치 함을 확인 후 호출되는 함수이기 때문에 마지막 문자 바로 전부터 검사 
    for i in range(len(pattern)-2, -1, -1):
        if pattern[i] == char:      # 불일치 문자가 패턴 문자열에 있는 경우
            return len(pattern)-i-1 # 뒤에서 i번째 있으므로 (i-1)만큼 skip
    
    return len(pattern)             # 패턴에 없는 문자이므로 패턴 길이만큼 skip


# 테스트
print(boyer_moore("bye","heyhibye"))    # expected output: True
print(boyer_moore("hello", "heyhibye")) # expected output: False
    