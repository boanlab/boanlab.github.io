// nqueen 문제 - 8퀸 문제가 아닌, n퀸 문제입니다. (백준 9663번)

package main

import (
	"fmt"
	"math"
)

var N int
var count int = 0
var arr []int // 슬라이스(동적 배열) 선언

func nQueen(depth int) {
	// 모든 행에 Queen이 놓이면 count 를 +1 하고 return
	if depth == N {
		count++
		return
	}

	for i := 0; i < N; i++ {
		arr[depth] = i

		// 퀸이 놓일 수 있는 위치라면 재귀호출
		if Possibility(depth) {
			nQueen(depth + 1)
		}
	}
}

func Possibility(col int) bool {

	for i := 0; i < col; i++ {
		// 해당 열의 행과 i열의 행이 일치하는 경우 (같은 행의 존재 하는 경우)
		if arr[col] == arr[i] {
			return false
		}

		if math.Abs((float64)(col-i)) == math.Abs((float64)(arr[col]-arr[i])) { // math 패키지 함수는 모두 실수 연산만 가능(float 필수)
			return false
		}
	}
	return true
}

func main() {

	fmt.Scanln(&N)

	arr = make([]int, N)

	nQueen(0)
	fmt.Println(count)

}
