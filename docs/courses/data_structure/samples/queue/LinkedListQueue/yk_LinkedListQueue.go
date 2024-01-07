package main

import (
	"container/list"
	"fmt"
)

type Queue struct {
	l *list.List // 포인터 타입의 list 를 갖는 큐로
}

func NewQueue() *Queue {
	return &Queue{list.New()} // 큐 (리스트로) 생성
}

func (q *Queue) Enqueue(value interface{}) {
	q.l.PushBack(value)
}

func (q *Queue) Pop() interface{} {
	front := q.l.Front()
	if front != nil {
		return q.l.Remove(front)
	}
	return nil
}

func main() {

	queue := NewQueue()

	for i := 1; i < 8; i++ {
		queue.Enqueue(i) // 1~7 값을 큐에 인큐
	}

	r := queue.Pop()
	for r != nil {
		fmt.Printf("%v -> ", r)
		r = queue.Pop()
	}
}
