# -*- coding: utf-8 -*-

"""
题目：
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii

"""

### 解题思路：
	# 判断数组中， 是否存在两个不同的索引 i, j
	# 满足如下条件：
	#   1. nums[i] == nums[j]
	#   2. |i-j| <= k

# 1. 第一种思路，直接进行爆破，两次遍历找出符合条件的数据 -- 这种在 python 中会超时，时间复杂度
#    为 O(n^2)
# 2. 第二种就是利用 hash 表，遍历一次就可以得到结果：
#    a. 条件1的 nums[i] == nums[j], 可以通过 in 来判断是否在hash 表中直接进行判定
#    b. 条件2 则直接进行判断即可
# 代码如下：


# 第一种： 爆破：
def containsNearbyDuplicate1(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and abs(i-j) <= k:
                return True
    
    return False

# 第二种： 利用 hash
def containsNearbyDuplicate2(nums, k):
    hashtable = {}

    for i in range(len(nums)):
        if nums[i] in hashtable and abs(i-hashtable[nums[i]] <= k):
            return True
        else:
            hashtable[nums[i]] = i
    
    return False


if __name__ == "__main__":
	nums1, k1 = [1, 2, 3, 1], 3
	nums2, k2 = [1, 0, 1, 1], 1
	nums3, k3 = [1, 2, 3, 1, 2, 3], 2

	print(containsNearbyDuplicate2(nums1, k1))
	print(containsNearbyDuplicate2(nums2, k2))
	print(containsNearbyDuplicate2(nums3, k3))