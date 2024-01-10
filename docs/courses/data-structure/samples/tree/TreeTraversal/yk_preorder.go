package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func preorderTraversal(root *TreeNode) []int {

	result := []int{}

	var preorder func(*TreeNode)

	preorder = func(root *TreeNode) { // 함수 리터럴 사용 (람다 느낌)
		if root == nil {
			return
		}

		result = append(result, root.Val)
		preorder(root.Left)
		preorder(root.Right)
	} // 여기까지가 함수

	preorder(root)

	return result
}
