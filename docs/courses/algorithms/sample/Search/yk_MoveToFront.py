def move_to_front(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            for j in range(i-1,-1,-1):  # key 값의 앞 부분만 뒤로 한 칸씩 밀리면 된다.
                arr[j+1] = arr[j]
            arr[0] = key # 맨 처음 값은 key값으로
            return i
    return False

arr = [1,4,5,6,8,12,34,2]

x = 12

res = move_to_front(arr,x)

if not res:
    print("Not Found")
else:
    print("index : ", res)
    print("arr : ", arr)
