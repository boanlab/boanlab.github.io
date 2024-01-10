
def divide(list):

    if len(list) <= 1:
        return list

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    left_completed = divide(left)
    right_completed = divide(right)
    return merge(left_completed,right_completed)


def merge(left,right):

    result = []         # 결과를 담을 리스트

    while len(left) > 0 or len(right) > 0:      # 분할한 리스트(왼쪽/오른쪽) 길이가 0보다 크다면 반복
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:     # 왼쪽 리스트의 처음 값이 더 작으면
                result.append(left[0])
                left = left[1:]         # 결과 리스트에 넣은 값은 삭제
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result
