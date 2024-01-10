package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func postorderTraversal(root *TreeNode) []int {

	result := []int{}

	var postorder func(*TreeNode)

	postorder = func(root *TreeNode) {
		if root == nil {
			return
		}

		postorder(root.Left)
		postorder(root.Right)
		result = append(result, root.Val)
	}

	postorder(root)

	return result

}
