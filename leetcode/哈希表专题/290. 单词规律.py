# -*- coding: utf-8 -*-

"""
题目：
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false

示例 4:
输入: pattern = "abba", str = "dog dog dog dog"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern

"""

## 解题思路
## 也是一个映射关系， 将s中每个单词和 pattern 中每个字符做个映射， 如果能匹配上则遵循相同的规律
## 代码如下

def wordPattern(p, s):
    s = s.split()

    if len(p) != len(s):
        return False
    
    hashtable = {}

    for i in range(len(p)):
        if p[i] in hashtable:
            if s[i] != hashtable[p[i]]:
                return False

        else:
            if s[i] in hashtable.values():
                return False
            else:
                hashtable[p[i]] = s[i]
    
    return True


if __name__ == "__main__":
	p1 = 'abba'
	s1 = "dog cat cat dog"

	p2 = 'abba'
	s2 = "dog cat cat fish"

	p3 = "aaaa"
	s3 = "dog cat cat dog"

	p4 = 'abba'
	s4 = "dog dog dog dog"

	print(wordPattern(p1, s1))
	print(wordPattern(p2, s2))
	print(wordPattern(p3, s3))
	print(wordPattern(p4, s4))