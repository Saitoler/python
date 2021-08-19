# -*- coding: utf-8 -*-
from collections import Counter

"""
题目：
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例 1：
输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。

示例 2：
输入：s = "", t = "y"
输出："y"

示例 3：
输入：s = "a", t = "aa"
输出："a"

示例 4：
输入：s = "ae", t = "aea"
输出："a"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-difference
"""

### 解题思路：
# 可以利用集合的思想，来求补集，可找到被添加的字母

def findTheDifference(s, t):
    sCount = Counter(s)
    tCount = Counter(t)

    if len(s) > len(t):
        return "".join(list((sCount-tCount).elements()))
    else:
        return "".join(list((tCount-sCount).elements()))


if __name__ == "__main__":
    s = 'abcd'
    t = 'abcde'

    print(findTheDifference(s, t))