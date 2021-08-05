# -*- coding: utf-8 -*-

"""
题目：
给你两个二进制字符串，返回它们的和（用二进制表示）。输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
 

提示：
每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4；字符串如果不是 "0" ，就都不含前导零。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
"""


### 解题思路：
# 要先转int, 加完再转回二进制， 这种思路对于算法题的练习来说意义不大，这里提供一种从末尾相加的思路：

# 两个位置相加有几种情况？
# 0+0 = 0
# 0+1 = 1
# 1+1 = 2
# 还有最后一种， 1+1+1(进位) = 3
# 想清楚以上几种情况是比较关键的
# 如果两个字符串长度相等，直接循环没问题。那如果长度不相等呢？你循环里加着加着突然较短的字符串没有地方去让你加就会导致数组越界。
# 所以思路就是，先对较短的那个字符串做“加长”处理，在短字符串的前面位置填充 ‘0’,直到两者等长
# 以上两者想清楚后，还有最后一个点了，就是怎么处理进位？什么时候要进位？
# 0+0， 不进位，或者说进位 = 0
# 0+1， 不进位，或者说进位 = 0
# 1+1， 进位 = 1， 原位置 = 0
# 1+1+1， 进位 =1， 原位置 = 1

def addBinary(a, b):
    if len(a) > len(b):
        result = list(a)
        b = list('0'*(len(a)-len(b))+b)
    else:
        result = list(b)
        a = list('0'*(len(b)-len(a))+a)
    
    index = len(a)-1
    plus = 0

    while index >= 0:
        strAdd = plus+int(a[index])+int(b[index])
        if strAdd == 2:
            result[index] = '0'
            plus = 1
        elif strAdd == 3:
            result[index] = '1'
            plus = 1
        else:
            result[index] = str(strAdd)
            plus = 0
        index -= 1
    
    if plus == 1:
        result.insert(0, '1')
    
    return "".join(result)


if __name__ == "__main__":
    a1 = '1011'
    b1 = '1111001'
    
    a2 = "11"
    b2 = "1"

    a3 = '1111'
    b3 = '1111'

    print(addBinary(a1, b1))
    print(addBinary(a2, b2))
    print(addBinary(a3, b3))