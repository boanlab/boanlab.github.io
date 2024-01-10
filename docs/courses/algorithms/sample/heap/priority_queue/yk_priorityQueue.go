package main

import (
	"container/heap"
	"fmt"
)

type Heap []int // golang 은 java와 달리 implements 키워드 X , interface의 메서드만 구현하면 알아서 판단해준다.

func (h Heap) Len() int {
	return len(h) // 슬라이스의 길이를 구함
}

func (h Heap) Less(i, j int) bool {
	r := h[i] < h[j] // -> min heap 생성 / h[i] > h[j] 면 max heap
	return r
}

func (h Heap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i] // 값의 위치를 바꿈
}

func (h *Heap) Push(x interface{}) {
	*h = append(*h, x.(int)) // 맨 마지막에 값 추가
}

func (h *Heap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]     // 슬라이스의 맨 마지막 값을 가져옴
	*h = old[0 : n-1] // 맨 마지막 값을 제외한 슬라이스를 다시 저장
	return x
}

func main() {
	data := new(Heap) // 힙 생성

	heap.Init(data)    // 힙 초기화
	heap.Push(data, 3) // 힙에 데이터 추가
	heap.Push(data, 2)
	heap.Push(data, 7)
	heap.Push(data, 10)

	fmt.Println(data, "최솟값 : ", (*data)[0]) // 최댓값을 구한다면 max heap (Less 함수) 으로 위의 코드를 변경하면 된다.
}
