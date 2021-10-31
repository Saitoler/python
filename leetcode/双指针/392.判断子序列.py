# -*- coding: utf-8 -*-

"""

给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形
成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""


def f(s, t):
	# 使用双指针的思路解决
	# i 指针指向 s 的开头， j 指针指向 t 的开头
	# 然后 s[i] 和 t[j] 相比较：
	#   如果 s[i] == t[j], 则 i 右移，j 右移一位
	#   如果 s[i] != t[j], 则 j 右移一位，继续与t 后面的元素相匹配
	# 到最后如果 i 移动到了 s 的末尾，则证明 s 是 t 的子序列

	i, j = 0, 0

	while i < len(s) and j < len(t):
		if s[i] == t[j]:
			i += 1
		j += 1

	return i == len(s)


if __name__ == "__main__":
	print(f('ace', 'abcde'))
	print(f('axc', 'ahbgdc'))