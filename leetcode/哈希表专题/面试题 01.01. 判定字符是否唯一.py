# -*- coding: utf-8 -*-

"""
题目：
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：
输入: s = "leetcode"
输出: false

示例 2：
输入: s = "abc"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-unique-lcci

"""

## 解题思路：
## 方法1: 利用 Set 的特性，如果有重复字符会自动去重，导致与原字符串的长度不相等
## 方法2: 遍历一遍数组，如果找到有重复出现的字符，直接返回 False

# 代码如下

# 方法1
def isUnique1(astr):
    return len(astr) == len(set(astr))

# 方法2
def isUnique2(astr):
    strList = []
    for c in astr:
        if c in strList:
            return False
        strList.append(c)
    
    return True
