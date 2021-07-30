# -*- coding: utf-8 -*-
from functools import reduce

"""
题目：

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number

"""

### 解题思路：
### 线性时间复杂度即 O(1) 的时间复杂度， 还要不使用额外空间， 暂时没想到，不过可以使用 hash 来实现
###  - 遍历数组中每个元素，如果该元素不在 dict 中，就将其以数组中元素值为键，任意值为key 加入到 dict 中
###  - 如果该元素存在，那就从 dict 中将其删除，最终剩下的就是唯一出现依次的元素了。

###   --- 这种方法的时间复杂度为 O(n), 且开了额外的空间-dict

def singleNumber(nums):
    hashtable = dict()

    for i in range(len(nums)):
        if nums[i] not in hashtable.keys():
            hashtable[nums[i]] = 1
        else:
            hashtable.pop(nums[i])
    
    return [k for k, v in hashtable.items() if v == 1][0]

### 看了题解后，终于知道这道题的设计的点在哪里，这道题完全就是设计出来考察异或运算的： "除一个数字出现一次，其他数字都出现两次"
### 在 python 中，异或运算符： ^
### 让我们复习下异或的基本知识：
### 1. 异或运算，是将两个数转换为二进制后各位上每一位相异或，两对应的位不同时，结果为1， 相同时则结果为0
### 2. 0 与任何数异或，都等于这个数： 即 0^a = a
### 3. 任何数与其本身异或，结果都为0，因为每一位都相同，每一位的结果都为0
### 4. 异或满足交换律和结合律：  即 a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b

### 了解了如上的背景知识，这道题是不是简直是为异或算法量身定做的，代码如下：


def singleNumber2(nums):
    def fn(x, y):
        return x^y
    
    # 给数组排个序，这样计算的时候能极大简化计算复杂度
    nums.sort()
    return reduce(fn, nums)


if __name__ == "__main__":
    print(singleNumber2([2,2,1]))