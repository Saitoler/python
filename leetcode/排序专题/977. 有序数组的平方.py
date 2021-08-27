# -*- coding: utf-8 -*-

"""
题目：
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，
要求也按 非递减顺序 排序。

示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array


"""


# 解题思路：
# 其实很简单， 先做平方运算，再进行排序，因为数组中有负数

def sortedSquares(nums):
    return sorted(list(map(lambda x: x*x, nums)))


if __name__ == "__main__":
    nums = [-7,-3,2,3,11]
    print(sortedSquares(nums))