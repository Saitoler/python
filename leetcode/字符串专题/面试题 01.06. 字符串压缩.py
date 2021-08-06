# -*- coding: utf-8 -*-

"""
题目：

字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:
 输入："aabcccccaaa"
 输出："a2b1c5a3"

示例2:
 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。

提示：
字符串长度在[0, 50000]范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compress-string-lcci

"""

### 
# 这道题的解题思路比较简单：

# 遍历整个字符串，统计每个字符是否有重复出现，构造压缩字符串
# 构造完成后判断压缩后的字符串是否变短， 若未变短，返回原字符串
# --- 这里要注意，变短的意思是，压缩后字符串长度 <= 原字符串长度，这里的判断不要出错

def compressString(s):
    if not s:
        return s
    
    resultChar = ""
    keyChar = s[0]
    keyCount = 1

    for i in range(1, len(s)):
        if s[i] == keyChar:
            keyCount += 1
        else:
            resultChar += (keyChar+str(keyCount))
            keyChar = s[i]
            keyCount = 1
    
    compressChar = resultChar + keyChar + str(keyCount)
    if len(compressChar) >= len(s):
        return s
    else:
        return compressChar


if __name__ == "__main__":
    s1 = "aabcccccaaa"
    s2 = "abbccd"
    s3 = ""

    print(compressString(s1))
    print(compressString(s2))
    print(compressString(s3))