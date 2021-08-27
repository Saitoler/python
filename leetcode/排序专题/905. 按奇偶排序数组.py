# -*- coding: utf-8 -*-

"""
给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
你可以返回满足此条件的任何数组作为答案。

示例：
输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-parity
"""

### 解题思路：
# 最基础的思路，新开两个数组，分别保存奇数和偶数，再合并数组，时间复杂度是 O(n)
# 代码如下：

def sortArrayByParity1(nums):
    # 偶数数组
    oddNums = []

    # 奇数数组
    nonOddNums = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            oddNums.append(nums[i])
        else:
            nonOddNums.append(nums[i])
    
    for i in range(len(nonOddNums)):
        oddNums.append(nonOddNums[i])

    return oddNums

## 方法2:
# 按照奇偶排序，可以简单的使用 % 2 的结果去进行排序，这样子可以通过一遍扫描就得出结果：

def sortArrayByParity2(nums):
    nums.sort(key=lambda x: x%2)
    return nums


if __name__ == "__main__":
    nums1 = [3, 1, 2, 4]

    print(sortArrayByParity1(nums1))
    print(sortArrayByParity2(nums1))