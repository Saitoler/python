# -*- coding: utf-8 -*-

"""
给你二叉树的根节点 root ，返回它节点值的前序遍历。


示例 1：
输入：root = [1,null,2,3]
输出：[1,2,3]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]

示例 5：
输入：root = [1,null,2]
输出：[1,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def preorderTraversal(tree):
	# 非递归
	result, stack = [], []

	while tree or stack:
		while tree:
			result.append(tree.val)
			stack.append(tree)
			tree = tree.left

		if stack:
			t = stack.pop()
			tree = t.right


	return stack

	# 递归：
	result = []

	def preorder(tree):
		result.append(tree.val)
		preorder(tree.left)
		preorder(tree.right)

	preorder(tree)

	return result