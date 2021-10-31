# -*- coding: utf-8 -*-
from functools import reduce

"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为 1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。

示例 1：
输入：19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

示例 2：
输入：n = 2
输出：false

提示：
1 <= n <= 231 - 1


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

## 解题思路：
# 基础解题思路：
# 对每一位上的数求平方和这个都好算，这道题的关键在于如何检测是否有循环，这个是难点
# 我们可以用一个哈希表，将算出来的值，加入该哈希表，在加入前先判断一下表中是否有算出来的值
# 如果有，则肯定会有循环，想通了这一点，就很容易写出来了

def isHappy(n):
	hashtable = {}

	while n != 1:
		strNum = str(n)
		n = reduce(lambda x,y:x+y, map(lambda x:x*x, map(int, strNum)))
		if n in hashtable:
			return False
		else:
			hashtable[n] = 1
	return True


if __name__ == "__main__":
	print(isHappy(19)) # True
	print(isHappy(2))  # False