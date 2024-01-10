'''
Quick-Select 알고리즘을 구현한 quick_select 메소드
n개의 원소로 이루어진 리스트에서 k번째로 작은 원소를 찾을 수 있음
'''
def quick_select(array, k):
    # array의 첫 번째 원소를 pivot으로 정함
    pivot = array[0]
    '''
    pivot보다 크기가 작은 원소들을 저장하는 left 리스트
    pivot보다 크기가 큰 원소들을 저장하는 right_array 리스트
    pivot과 같은 원소들을 저장하는 same_array 리스트
    '''
    left, right, same_array = [], [], []

    for x in array:
        if pivot > x: left.append(x)
        elif pivot < x: right.append(x)
        else: same_array.append(x)

    # 찾고자 하는 원소가 pivot보다 작을 때 left 리스트에서 quick_select 메소드 재귀 호출
    if len(left) > k-1: return quick_select(left, k)
    # 찾고자 하는 원소가 pivot보다 클 때 right 리스트에서 quick_select 메소드 재귀 호출
    elif len(left) + len(same_array) < k: return quick_select(right, k-2-len(left)+len(same_array))
    else: return pivot

# 테스트
test_array = [4, 10, 24, 9, 522, 2, 73, 39, 6, 12]
# 최소값 출력(리스트의 첫 번째로 작은 원소 출력)
print(quick_select(test_array, 1))  # expected output: 2