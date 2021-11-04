# -*- coding: utf-8 -*-

"""
给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。


示例 1：

输入：s = "abcdefg", k = 2
输出："bacdfeg"
示例 2：

输入：s = "abcd", k = 2
输出："bacd"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

### 解题思路，这道题很匹配 python 的 range 函数及数组切片的思想，直接按照题目思路进行模拟即可

def reverseStr(s, k):
	listStr = list(s)

	for i in range(0, len(s), 2*k):
		listStr[i:i+k] = reversed(listStr[i:i+k])

	return "".join(listStr)


if __name__ == "__main__":
	s1, k1 = "abcdefg", 2
	s2, k2 = "abcd", 2

	print(reverseStr(s1, k1))
	print(reverseStr(s2, k2))
