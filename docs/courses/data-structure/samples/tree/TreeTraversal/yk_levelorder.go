type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {

	result := [][]int{}

	queue := []*TreeNode{root}

	for len(queue) != 0 {

		level := []int{} // 반복문안에 선언했으므로 초기화 반복 (result 에 레벨별로 저장되게끔)
		qlength := len(queue)

		for i := 0; i < qlength; i++ {
			if queue[0] != nil {
				level = append(level, queue[0].Val)
				queue = append(queue, queue[0].Left)
				queue = append(queue, queue[0].Right)
			}
			queue = queue[1:] // 처리한 큐 값은 삭제
		}
		result = append(result, level)
	}

	return result[:len(result)-1] // 마지막 반복에서 nil 값이 삽입되기 때문에 마지막 리스트는 제거
}