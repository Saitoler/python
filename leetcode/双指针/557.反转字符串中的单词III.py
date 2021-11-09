# -*- coding: utf-8 -*-

"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。


示例：
输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

提示：
在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 这道题理论上不应该归类在双指针这里，应该归类在字符串或数组那边吧
# 思路就是：
# 1. 因为Python中字符串是不可变对象，因为将字符串先按空格分隔后转换在数组中即可
# 2. 然后对每个单词进行反转，可以直接使用切片进行反转
# 3. 最后再重新将数组转换为字符串输出

def reverseWords(s):
	listStr = list(s.split())
	for i in range(len(listStr)):
		listStr[i] = listStr[i][::-1]

	return " ".join(listStr)


if __name__ == "__main__":
	print(reverseWords("Let's take LeetCode contest"))