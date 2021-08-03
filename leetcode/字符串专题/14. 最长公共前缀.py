# -*- coding: utf-8 -*-

"""
题目：

编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix

""" 

### 解题思路：
### 这道题是要找出数组中的最长公共子序列，拿到题后怎么思考呢？
### 1. 先假设这个数组中只有两个字符串，那就是在这两个字符串中找公共子序列
### 2. 再假设这个数组中加入第三个字符串，如何寻找公共子序列？ 就是在1得到的结果上，再与第三个字符串计算，获得一个公共子序列
### 3. 以此类推，就是遍历整个数组，分别计算公共子序列，到最后得到的结果就是整个数组的最长公共子序列

# 代码如下：
## 先写一个子函数来计算两个字符串的公共子序列
##   ： 公共子序列肯定在相对长度较小的字符串中
##   ： 以长度较小的字符串的长度为循环次数，逐个字符串比较，直到不一样就停止下来。


def longestCommonPrefix(strs):
    def getPrefix(str1, str2):
        length = min(len(str1), len(str2))
        index = 0

        while index < length:
            if str1[index] == str2[index]:
                index += 1
            else:
                break
        return str1[:index]
    

    prefix = strs[0]
    for i in range(1, len(strs)):
        prefix = getPrefix(prefix, strs[i])
        if not prefix:
            break

    return prefix


if __name__ == "__main__":
    strs1 = ["flower","flow","flight"]
    strs2 = ["a", 'b', 'c']
    print(longestCommonPrefix(strs1))
    print(longestCommonPrefix(strs2))

