# -*- coding: utf-8 -*-

"""
题目：

给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array

"""

### 之前有道题，是找数组中是否存在该值，若不存在，插入到其中，可以用到这里来。
### 整体的思路其实就是：
### 1. 给 nums2 数组中的每一个元素，都在 nums1 中找到一个合适的位置，并插入
### 2. 由于在插入 nums1 中时，nums1 的有效元素个数是递增的，所以每次执行insert 时的搜索位置时，要搜索的范围要定义好（因为有0是占位符，所以要对搜索范围做处理）
### 3. 每插入一个值，为了达到替换的目的， 就可以将原数组中站位的位于末尾的0，pop() 出去，这样最终得到的 nums1, 就是一个完整的具有 m+n 元素的数组了。


def merge(nums1, m, nums2, n):
    def searchInsert(nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high)//2
            if  nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return low
    for i in range(len(nums2[:n])):
        nums1.insert(searchInsert(nums1[:m+i], nums2[i]), nums2[i])
        nums1.pop()


if __name__ == "__main__":
     nums1 = [1, 2, 4, 6, 0, 0, 0]
     nums2 = [2, 5, 7, 0, 0]
     merge(nums1, 4, nums2, 3)
     print(nums1)

    