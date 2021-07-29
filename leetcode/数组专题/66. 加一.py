# -*- coding: utf-8 -*-

"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。


示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
"""

### 解题思路：
### 首先想到的就是 a python way to solve, 用 python 处理这种问题相对简单：
###  1. 先将数组转换成字符串
###  2. 再将字符串转换成int类型，加1
###  3. 将+1的结果再转换成字符串，逐个放入数组时将每个元素再转换成int 类型
### 代码如下：
def plusOne(digits):
    numStr =  ""
    for i in range(len(digits)):
        numStr += str(digits[i])
    print("----mapstr result is {}".format(list(map(str, digits))))
    resultStr = str(int(numStr)+1)

    resultList = []
    for ch in resultStr:
        resultList.append(int(ch))
    return resultList

### actually, 上面的代码完全可以用 map() 去做到在一行中实现，如下：

def plusOne2(digits):
    return list(map(int, list(str(int("".join(map(str, digits)))+1))))

### 看了题解后，这道题其实是为了考察数组中元素相加要考虑进位的知识点，上面用python 
### 只能说刚好 取巧解决了这个问题。

### 对于题目来说，没有0开头的数组，那对于所有的元素来讲，加1仅仅就有两种情况：
###  1.  当前位是 9， 加1后导致进位，然后当前位  置 0
###  2.  当前位非 9， 则正常加1, 直接返回
###  3.  像 99 这样的数，加1后会变成100，导致数组扩大一位，需要往最前面插入数据 ，其他位都置0

### 代码如下：

def plusOne3(digits):
    i = len(digits)-1

    while i >= 0:
        digits[i] += 1
        if digits[i] % 10 == 0:
            digits[i] = 0
            i -= 1
        else:
            return digits
    
    digits.insert(0, 1)
    return digits


if __name__ == "__main__":
    print(plusOne3([1,2,3]))
    print(plusOne3([9, 9]))
    print(plusOne3([9]))


