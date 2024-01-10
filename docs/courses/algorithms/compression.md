---
layout: default
title: AdaBoost
parent: Algorithms
grand_parent: Courses
---

# Compression
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# 데이터 압축 (Data Compression)


## 데이터 압축

- 데이터를 더 적은 저장 공간에 효율적으로 기록하기 위한 기술

**손실 압축** : 중복되고 필요하지 않은 정보가 손실되는 것을 허용

**무손실 압축** : 자료의 손실이 없으며 입출력 영상이 완전히 동일하도록 압축

- 반복 길이 부호화
- 허프만 부호화
- 산술 부호화


</br>

## RLE(Run-Length encoding)

### 정의

- **동일한 패턴이 반복**되는 문자열을 압축하는 알고리즘
- **무손실 압축** 방법 중의 하나

### 예시

- aaabbcccc → 3a2b4c

### 코드(simple)

```python
def rle(st):
    n = len(st)
    i = 0
    while i < n - 1:
				
        count = 1
        while (i < n - 1 and st[i] == st[i + 1]): # 반복 비교하면서 count 체크
            count += 1
            i += 1
			
        print(st[i] +str(count),end="") # count 완료되면 바로 출력

        i += 1
```

</br>

#

## 허프만 코딩 (Huffman Coding)

### 정의

- **무손실 압축** 방법 중 하나
- 원본 데이터에서 출현 빈도가 **높은** 문자 => **적은** 비트의 코드로 변환
- 원본 데이터에서 출현 빈도가 **낮은** 문자 => **많은** 비트의 코드로 변환
- 전체 데이터를 표현하는데 필요한 비트 수를 줄이는 방법

</br>

### 용어


**접두부 (prefix code)**

- 각 문자에 부여된 이진 코드가 다른 문자에 부여된 이진 코드의 접두부가 되지 않는 코드
- 즉, 겹치지 않도록 이진 코드를 만드는 것
```
a - > 101
b -> 1, 10, 101은 부여 X
```
- 각 문자가 접두부가 되어야만 디코딩 과정에서 문제 발생 X

</br>

**인코딩 (encoding) 과 디코딩 (decoding)**

- 인코딩

	- aabbcc => 11101000

- 디코딩

 	- 11101000 => aabbcc

</br>

**허프만 트리**

- 상향식으로 만드는 이진트리로 욕심쟁이방법(Greedy Algorithm)을 사용한 완전이진트리

</br>

### 원리

**허프만 트리 구현 방법**

```
1. 각 문자가 개별적인 트리인 상태에서 시작 ( 리프노드 )
2. 각 노드는 빈도 수를 표시
3. 빈도 수가 작은 두 트리를 합쳐서 부모노드를 생성
4. 좌우 간선은 0과 1로 써줌 => (이진화 할때 사용)
5. 부모노드의 빈도 수는 두 자식 노드의 빈도 수 합
```

</br>

### 예시


						"aaabrbacard"
						
<p align="center"><img src="https://user-images.githubusercontent.com/113777043/210158999-c54a3246-57a3-4fa1-bb3e-86bce80e6bca.png"></p>

| 문자 | 코드 |
| :---: | :---: |
| a | 0 |
| b | 100 |
| c | 110 | 
| d | 111 |
| r | 101 |

**결과**

aaabrbacard => 00010010110001100101111 ( 23 bit )

</br>

### 단점

- 각 문자의 빈도수를 모르는 경우 주어진 텍스트를 2번 읽음
	- 각 문자의 빈도수 계산
	- 텍스트를 읽으며 실제로 인코딩 할 때
	
	
### 시간 복잡도

- 허프만 트리를 만드는 시간 = O(nlogn)
	- n은 문자집합의 크기
- 길이가 m 인 텍스트의 인코딩 시간 = O(m)
- 총 시간 복잡도 = O(nlogn + m)

## 동적 허프만 코딩(Adaptive Huffman Coding)

### 특징

- 동적 허프만 트리는 실시간으로 만들어지며, input값을 읽고 트리를 만드는 과정이 동시에 이루어진다.
- 각 문자에 대한 빈도수를 다 알지 못하므로 root에서 시작해서 아래로 잎을 만들며 Tree를 구성한다.

### 원리

1. 새롭게 추가되는 문자라면 null node를 사용하여 트리에 추가한다.(맨 아래 좌측 노드에)
2. 이미 있는 요소라면 단순히 frequency를 1 증가시킨다.
3. frequency를 증가시켰을 때 left to right/bottom to top 조건에 위배된다면 두 노드를 swap한다.
