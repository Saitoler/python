# -*- coding: utf-8 -*-

"""
题目：

实现 strStr() 函数。
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

说明：
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

示例 1：
输入：haystack = "hello", needle = "ll"
输出：2

示例 2：
输入：haystack = "aaaaa", needle = "bba"
输出：-1

示例 3：
输入：haystack = "", needle = ""
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
"""

## 这道题就是典型的字符串模式匹配的问题了，KMP算法看了半天理解不了……，先用爆破方法来解决吧。。
### 思路就是，从主串中第一个元素开始进行模式串的匹配，如果没匹配到：
### 1. 主串中的值移动到下一个元素
### 2. 模式串中的下标从头开始：

## 注： python 代码的爆破会超时 ...
def strStr(haystack, needle):
    # needle 为空，返回 0
    if not needle:
        return 0
    
    # needle 的长度大于 haystack， 返回 -1
    if len(needle) > len(haystack):
        return -1
    
    i, j = 0, 0
    while i < len(haystack) and j < len(needle):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            ## i-j+1, 从主串中去掉已经匹配过的字串中的元素个数j个，加1就是从下一个开始重新匹配
            ## 同理，首次出现的位置，就是 i-j
            i = i-j+1 
            j = 0
    
    if j == len(needle):
        return i-j
    else:
        return -1


    
### 在 python 中，其实是有现成的方法可以使用的： str.find(s)

def strStr2(haystack, needle):
    if len(needle) == 0:
        return 0

    return haystack.find(needle)

### 还有一种利用遍历的方法，也是利用python 的切片机制来进行遍历，比第一种的爆破的效率会高很多，因为只遍历一次，没有来回回溯i指针的浪费

def strStr3(haystack, needle):
    if not needle:
        return 0
    
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle[:]:
            return i
    
    return -1


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"

    print(strStr(haystack, needle))
    print(strStr2(haystack, needle))
    print(strStr3(haystack, needle))


    