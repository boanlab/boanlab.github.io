# 전위법을 사용한 순차 탐색 메소드 transpose()
def transpose(array, x):
    for i in range(len(array)):
        if x == array[i]: # 탐색된 경우
            if i != 0:
                # 탐색된 값을 바로 앞 인덱스 값의 자리와 교환
                array[i], array[i-1] = array[i-1], array[i]  
            return i
    return False

# 테스트
test_array = [4, 10, 24, 0, 522, 2, 73, 39, 6, 12]
result = transpose(test_array, 522)

print(result)       # expected output: 4
print(test_array)   # expected output: [4, 10, 24, 522, 0, 2, 73, 39, 6, 12]
