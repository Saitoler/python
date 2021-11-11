# -*- coding: utf-8 -*-


"""

给定一个二叉树的根节点 root ，返回它的 中序遍历。



示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]


示例 4：
输入：root = [1,2]
输出：[2,1]

示例 5：
输入：root = [1,null,2]
输出：[1,2]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

### 解题思路：
# 采用非递归的形式，递归方式会有递归深度的限制


def inorderTraversal(tree):
	result, stack = [], []

	while tree or stack:
		stack.append(tree)
		tree = tree.left

	if stack:
		t = stack.pop()
		result.append(t.val)
		tree = t.right

	return result


# 递归思路：
def inorderTraversal(tree):
	# 要将数据保存在列表中
	result = []

	# 再写一个内置函数，用于递归
	def inorder(tree):
		# 先递归遍历左子树
		inorder(tree.left)
		# 再获取数据
		result.append(tree.val)
		# 再递归遍历右子树
		inorder(tree.right)

	# 调用内置递归函数
	inorder(tree) 

	return result 
