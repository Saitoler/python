# -*- coding: utf-8 -*-

"""
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：
输入: s1 = "abc", s2 = "bca"
输出: true

示例 2：
输入: s1 = "abc", s2 = "bad"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-permutation-lcci
"""


### 解题思路：
# 因为是重新排列后变成另一个字符，所以两个字符串包含的字符都是相同的
#    直接排序即可

def checkPermutation1(s1, s2):
    return sorted(s1) == sorted(s2)

