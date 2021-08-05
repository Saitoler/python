# -*- coding: utf-8 -*-

"""
题目：
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串

示例 2:
输入: "race a car"
输出: false
解释："raceacar" 不是回文串
 
提示：
1 <= s.length <= 2 * 105
字符串 s 由 ASCII 字符组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
"""

### 解题思路：
## 1. 先处理掉原字符串中的非字母或数字字符
## 2. 使用切片进行回文比较即可

def isPalindrome(s):
    alphalist = []
    for i in range(len(s)):
        if str.isalpha(s[i]) or str.isdigit(s[i]):
            alphalist.append(s[i])
    
    alphalist = list(map(str.lower, alphalist))
    return "".join(alphalist) == "".join(alphalist[::-1])


if __name__ == "__main__":
    str1 = 'ababa'
    str2 = 'abcd'
    str3 = "0P"

    print(isPalindrome(str1))
    print(isPalindrome(str2))
    print(isPalindrome(str3))