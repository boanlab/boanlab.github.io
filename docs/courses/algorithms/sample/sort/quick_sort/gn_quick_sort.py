def quick_sort(array):
    # 리스트의 크기가 0이나 1이면 리스트를 그대로 반환하고 종료 
    if len(array) <= 1: return array

    # array의 첫 번째 원소를 pivot으로 정하고, 나머지를 tail 변수에 할당
    pivot, tail = array[0], array[1:]

    # 리스트 표현식을 사용하여 pivot 기준 왼쪽 리스트와 오른쪽 리스트 분리
    left_array = [x for x in tail if  x <= pivot]   # pivot보다 크기가 작은 원소들을 저장하는 left_array 리스트
    right_array = [x for x in tail if x > pivot]    # pivot보다 크기가 큰 원소들을 저장하는 right_array 리스트

    # 재귀 호출을 이용
    return quick_sort(left_array) + [pivot] + quick_sort(right_array)

# 테스트
test_array = [4, 10, 24, 0, 522, 2, 73, 39, 6, 12]

print(test_array)               # expected output: [4, 10, 24, 0, 522, 2, 73, 39, 6, 12]   
print(quick_sort(test_array))   # expected output: [0, 2, 4, 6, 10, 12, 24, 39, 73, 522]