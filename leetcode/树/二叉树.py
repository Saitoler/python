# -*- coding: utf-8 -*-


"""
这份文档基于 Python 实现一个二叉树 数据结构，
然后使用递归、非递归两种方式来实现 二叉树的先序遍历、中序遍历、后序遍历

"""


# 定义二叉树

class TreeNode:
	"""
	 - 一个二叉树包含三个值：
	 - val: 节点的值
	 - left: 左子树，也是一个 TreeNode 结构
	 - right: 右子树，也是一个 TreeNode 结构
	"""

	def __init__(self, val):
		self.val = val
		self.left = None 
		self.right = None 


	# 获取节点的val:
	def get(self):
		return self.val 


	# 获取左子树：
	def getLeft(self):
		return self.left 

	# 获取右子树：
	def getRight(self):
		return self.right 

	# 左子树的 setter 函数
	def setLeft(self, node):
		self.left = node 

	# 右子树的 setter 函数
	def setRight(self, node):
		self.right = node 

	def __str__(self):
		return self.val 



# 生成一个二叉树
"""
树形状如下：
 	      	0
 	   1        2
 	3    4    5    6

"""
binaryTree = TreeNode(0)

binaryTree.setLeft(TreeNode(1))
binaryTree.setRight(TreeNode(2))

binaryTree.getLeft().setLeft(TreeNode(3))
binaryTree.getLeft().setRight(TreeNode(4))

binaryTree.getRight().setLeft(TreeNode(5))
binaryTree.getRight().setRight(TreeNode(6))


"""
递归遍历
"""

# 递归先序遍历
def preorderRecursiveReversal(tree):
	if not tree:
		return None 

	print(tree.get(), end=" ")
	preorderRecursiveReversal(tree.getLeft())
	preorderRecursiveReversal(tree.getRight())


# 递归中序遍历
def middleorderRecursiveReversal(tree):
	if not tree:
		return None

	middleorderRecursiveReversal(tree.getLeft())
	print(tree.get(), end=" ")
	middleorderRecursiveReversal(tree.getRight())


# 递归后序遍历
def postorderRecursiveReversal(tree):
	if not tree:
		return None 

	postorderRecursiveReversal(tree.getLeft())
	postorderRecursiveReversal(tree.getRight())
	print(tree.get(), end=" ")



"""
非递归遍历

"""

# 非递归先序遍历
def preorderReversal(tree):
	# result 中存储按先序遍历规则遍历的数据
    # stack 是用于压栈用的，用于记录访问过的栈
	result, stack = [], []


	# 先序遍历，按照 根->左->右 的顺序进行树的查询
    # 按照先序遍历的规则：
    # 如果 tree 为 None， 且 stack 中为空，则表明已经遍历完了
    # 否则就都进下面的循环

    # 这里就指， tree 不为空，或栈非空
	while tree or stack:
		# 如果 tree 非空，考察到 tree 这个节点
		while tree:
			# 就先将节点的元素加入到结果中
			result.append(tree.get())
			# 然后因为这个节点我们目前仅访问了根节点，需要记录下他，加入 stack 中暂存
			stack.append(tree)
			# 根节点访问完成后，继续访问左子树， 这个会一直深入到最底层叶子节点
            # 如果到了最底层的叶子节点，则这句 tree.getLeft() 返回的就是 None， 就意味着左子树已经遍历完成
            # 已经到了最底层的左子树了
			tree = tree.getLeft()

		# 这里就意味着，tree 为空，已经到了最底层的左子树了， 当前栈中势必是有数据的
		if stack:
			# 弹栈，返回值就是弹出的那个叶子节点，如果是最底层的左子树，那么getRight() 的结果依然是空，即 tree 还是空
            # 最底层左子树弹出后，上一个就是倒数第二层的根节点了，弹出，再获取他的右子树，依次向上递推，最终就按照了
            # 根-->左-->右 的顺序，将整个树遍历完成了
			t = stack.pop()
			tree = t.getRight()

	return result


# 非递归中序遍历
def middleorderReversal(tree):
	result, stack = [], []

	while tree or stack:
		while tree:
			stack.append(tree)
			tree = tree.getLeft()
		if stack:
			t = stack.pop()
			result.append(t.get())
			tree = t.getRight()

	return result


# 非递归后序遍历
def postorderReversal(tree):
	# result 保存结果， stack 用于暂存节点
	result, stack = [], []
	# 设置游标 lastVisit, 因为后序遍历在决定是否需要输出当前节点时，要先判断其左、右子树是否都已经遍历
	# 如果 lastVisit 等于当前考察节点的右子树，则表明该节点左右子树都已遍历完成，就可以输出当前节点。

	# 这个时候，就将 lastVisit 设置成当前节点，然后将 tree 置为空，下一轮就可以直接从栈中访问栈顶元素了。
	# 如果 lastVisit 不等于右子树，则说明要接着考虑右子树
	lastVist = tree  

	# tree 非空，或栈中非空
	while tree or stack:
		while tree:
			# 进来后，因为要先遍历左右子树，先将路径上的节点加入栈中
			stack.append(tree)
			tree = tree.getLeft()

		# 上面 while 循环结束的时候， 遍历到了这样一种情况：
		#  case1： 到了最底部的叶子，已经没有左子树、右子树了
		#  case2: 到了中间的叶子节点，这个叶子节点是没有左子树的

		# 那就将 tree 指向到栈顶的节点
		tree = stack[-1]
		# 然后判断栈顶的节点是否有右子树
		# 如果没有右子树，或者右子树就是 lastVisit, 则说明，栈顶节点已经可以直接输出了
		if tree.getRight() is None or tree.getRight() == lastVist:
			# 输出节点
			result.append(tree.get())
			# 弹栈，这个节点以及其左右子树都处理完了，不需要了
			stack.pop()
			# lastVisit 设置成栈顶节点，记录上次访问的
			lastVist = tree 
			# 因为当前节点处理完了，就继续向上回溯，把 tree 先置空
			tree = None 
		else:
		# 如果有右子树，就继续处理右子树
			tree = tree.getRight()

	return result 





"""
测试函数
"""
if __name__ == "__main__":
	"""
	递归方法测试
	"""
	preorderRecursiveReversal(binaryTree)
	print()

	middleorderRecursiveReversal(binaryTree)
	print()

	postorderRecursiveReversal(binaryTree)
	print()


	"""
	非递归方法测试
	"""
	print(preorderReversal(binaryTree))
	print(middleorderReversal(binaryTree))
	print(postorderReversal(binaryTree))