# -*- coding: utf-8 -*-

"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。


示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

### 解题思路
# 因为题目中是一个递增数组，可以使用双指针的思想，一个左指针，一个右指针
# sums = nums[left]+nums[right]
# 将结果和 target 去做比较，如果大于 target，说明值大了，那就将右指针左移，找一个小点的数去求和
# 如果小于 target，说明值小了，那就将左指针右移，找一个大点的数去求和

def twoSum(nums, target):
	left, right = 0, len(nums)-1

	while left < right:
		sums = nums[left]+nums[right]
		if sums == target:
			return nums[left], nums[right]
		elif sums > target:
			right -= 1
		else:
			left += 1



if __name__ == "__main__":
	nums = [2, 7, 11, 15]
	target = 18

	print(twoSum(nums, target))