package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {

	result := []int{}

	var inorder func(*TreeNode)

	inorder = func(root *TreeNode) {
		if root == nil {
			return
		}

		inorder(root.Left)
		result = append(result, root.Val)
		inorder(root.Right)
	}

	inorder(root)

	return result

}
