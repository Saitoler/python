# -*- coding: utf-8 -*-

"""
题目：

给你一个字符串 s，由若干单词组成，单词之间用单个或多个连续的空格字符隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

示例 1：
输入：s = "Hello World"
输出：5

示例 2：
输入：s = " "
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-last-word
"""

### 解题思路
# 这道题就很明显能用 str.split() 来进行分割，求最后所得数组的最后一个元素的长度即可
# 所以问题就在于要去掉末尾的空格， 在处理前，先用 str.strip() 去掉末尾的空格即可

def lengthOfLastWord(s):
    if not s:
        return 0
    
    return len(s.strip().split(" ")[-1])

## 上面的思路其实是用已有的 api 来做的，还有一种思路：
## 从后面往前匹配，也是先去掉后面的空格，从后往前找首次出现 " " 的地方结束，或回到 index=0 的位置：

def lengthOfLastWord2(s):
    s = s.strip()

    index = len(s)-1

    while index >= 0:
        if s[index] != ' ':
            index -= 1
        else:
            break
    
    return len(s)-1-index


if __name__ == "__main__":
    s1 = "   fly me   to   the moon  "
    s2 = "n a bbb"
    
    print(lengthOfLastWord2(s1))
    print(lengthOfLastWord2(s2))