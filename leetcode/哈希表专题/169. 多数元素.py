# -*- coding: utf-8 -*-

"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：[3,2,3]
输出：3
示例 2：

输入：[2,2,1,1,1,2,2]
输出：2
 

进阶：

尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
"""


### 解题思路：
# 基本的 hash 问题， 将所有数据统计到 dict 中，最后在 dict 中找出所谓的多数元素

def majorityElement(nums):
    majorResult = {}
    majorCount = len(nums)//2

    for i in range(len(nums)):
        if nums[i] in majorResult:
            majorResult[nums[i]] += 1
        else:
            majorResult[nums[i]] = 1
    
    return [k for k, v in majorResult.items() if v > majorCount][0]


if __name__ == "__main__":
    nums1 = [3, 2, 3]
    nums2 = [2, 2, 1, 1, 1, 2, 2]

    print(majorityElement(nums1))
    print(majorityElement(nums2))