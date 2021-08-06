# -*- coding: utf-8 -*-

"""
题目：
给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。
混合字符串 由小写英文字母和数字组成。

示例 1：
输入：s = "dfa12321afd"
输出：2
解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。

示例 2：
输入：s = "abc1111"
输出：-1
解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。
 

提示：
1 <= s.length <= 500
s 只包含小写英文字母和（或）数字。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/second-largest-digit-in-a-string
"""

### 解题思路：
# 比较简单，写下解题思路：

# 遍历一遍字符串， 将里面是数字字符的元素找到
# 找到后转换为 int， 非重复的加入到 list 中（相当于一个 set）
# 对数组进行排序
# 判断数组长度，如果小于2， 说明要么字符串中没有数字字符的元素，要么就只有一个数字出现， 则直接返回 -1
# 如果大于2， 则直接返回倒数第二位的值即可。


def secondMax(s):

	digits = []

	for c in range(len(s)):
		if str.isdigit(s[c]):
			if int(s[c]) not in digits:
				digits.append(int(s[c]))

	digits.sort()

	if len(digits) < 2:
		return -1
	else:
		return digits[-2]



if __name__ == "__main__":
	s1 = "dfa12321afd"
	s2 = "abc1111"

	print(secondMax(s1))
	print(secondMax(s2))
