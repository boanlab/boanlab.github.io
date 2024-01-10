package main

import "fmt"

type Stack []interface{}

func (st *Stack) IsEmpty() bool {
	return len(*st) == 0
}

func (st *Stack) Push(value interface{}) {
	*st = append(*st, value)
}

func (st *Stack) Pop() interface{} {
	if st.IsEmpty() {
		fmt.Println("스택이 빈 상태입니다.")
		return nil
	} else {
		top := len(*st) - 1
		value := (*st)[top]
		*st = (*st)[:top] // 꺼낸 데이터 제거
		return value
	}
}

func main() {

	var stack Stack

	stack.Push(5)
	stack.Push(7)
	stack.Push(9)

	fmt.Println("Pop 결과 : ", stack.Pop())
	fmt.Println("Pop 결과 : ", stack.Pop())
	fmt.Println("Pop 결과 : ", stack.Pop())
	fmt.Println("Pop 결과 : ", stack.Pop())
}
