# 분할 정복(재귀)를 이용한 거듭제곱 메소드
def power(c, n):
    if n == 1:          # 지수 n이 1인 경우
        return c
    else:
        x = power(c, n//2)

        if n % 2 == 0:  # 지수 n이 짝수인 경우
            return x * x
        else:           # 지수 n이 홀수인 경우
            return x * x * c

# 테스트
print(power(10, 3)) # expected output: 1000

