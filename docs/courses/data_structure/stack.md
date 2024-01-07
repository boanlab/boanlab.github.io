---
layout: default
title: Stack
parent: Data_Structure
grand_parent: Courses
---

# Stack

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

- TOC
  {:toc}

---

# 스택

### 정의

- 제한적으로 접근할 수 있는 나열 구조의 자료구조
  ![스택](https://images.velog.io/images/sbinha/post/17a3cf61-fb95-4970-b66c-92a71b99846b/Screenshot%202020-04-20%2019.07.55.png)

### 특징

- 접근은 목록의 끝에서만 가능하다.
- 한 쪽 끝에서만 자료를 넣거나 뺄 수 있는 선형 구조으로 되어 있다.
- 가장 최근에 삽입한 자료부터 나오는 LIFO(Last In First Out) 구조이다.

### 기본 연산 종류

- peek(): 스택의 가장 윗 데이터를 반환(스택이 비었다면 연산 정의불가)

- pop(): 스택의 가장 윗 데이터를 삭제(스택이 비었다면 연산 정의불가)
  ![스택](https://velog.velcdn.com/images%2Fwksh229%2Fpost%2F448a7369-f1f8-466e-9e28-02691ad61ba5%2FIMG_0224.jpg)

- push(): 스택의 가장 윗 데이터(top)에 메모리를 생성 후 데이터 삽입
  ![스택](https://velog.velcdn.com/images%2Fwksh229%2Fpost%2F2ea519a9-a28b-469a-87dd-f89e5134de16%2FIMG_0223.jpg)

- empty(): 스택이 비었는지 여부 확인(비었으면 1, 안 비었으면 0)

---

## 연결 리스트 기반 스택

### 장점

- 데이터의 삽입, 삭제가 용이하다.

### 단점

- 한 번에 원하는 데이터의 접근이 불가능하다.

---

## 배열 기반 스택

### 장점

- 메모리를 아낄 수 있고 구조가 간단하다.

### 단점

- 크기가 제한되어있다.
