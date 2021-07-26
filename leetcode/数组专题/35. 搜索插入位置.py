# -*- coding: utf-8  -*-

"""
题目：

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

 

示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:

输入: nums = [1,3,5,6], target = 2
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position

"""

### 解题思路

# 这题一看就是要用二分法呀。。。
# 这道题和之前的二分法不同的是，待搜索的元素有可能是不在数组中的，
# 对于在数组中的情况，一定能找到，返回那个 mid 即可
# 对于不在数组中的情况， 有三种：
#  a. 要插入到数组最左侧
#  b. 要插入到数组最右侧
#  c. 要插入到数组中间
#     以上三种情况，研究下来，返回值均为 low, 于是 while 循环中的返回就分两种情况
#       1. 能找到，在 while 循环中，返回 mid
#       2. 找不到，这种都突破了while 循环的循环条件，即 low > high 的情况了，返回 low


def searchInsert(nums, target):
    low, high = 0, len(nums)-1

    while low <=high:
        mid = (low+high)//2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid+1
        else:
            high = mid-1
    
    return low


        


