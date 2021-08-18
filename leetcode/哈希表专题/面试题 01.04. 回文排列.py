# -*- coding: utf-8 -*-
from collections import Counter

"""
题目： 
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
回文串不一定是字典当中的单词。

示例1：
输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation-lcci

"""

### 解题思路：
# 这道题一开始陷入了误区：
#   就是想把字符串中所有字符的所有组合都算出来，再逐一判断其中是否有回文串…… 这种效率太低太低了
# 看了题解，还是要抓住共性， 就是一个回文串，满足什么样的共性条件？

# 'a' : 是回文串，仅有一个奇数个的字符
# 'aa': 是回文串，没有奇数个的字符
# 你可以再枚举几个回文串，最后可以发现一个共性：
# 字符串中包含奇数个字符的数量，最多只有一个  --- 这就是我们这道题中要判断的

def canPermutePalindrome(s):
    countS = Counter(s)

    singleChar = len([k for k, v in countS.items() if v % 2 == 1])

    if singleChar <= 1:
        return True

    return  False