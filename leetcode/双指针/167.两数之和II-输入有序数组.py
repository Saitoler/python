# -*- coding: utf-8 -*-


"""
给定一个已按照 非递减顺序排列的整数数组 numbers ，请你从数组中找出两个数满足相加之和等
于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数,
所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。


示例 1：
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

示例 2：
输入：numbers = [2,3,4], target = 6
输出：[1,3]

示例 3：
输入：numbers = [-1,0], target = -1
输出：[1,2]


提示：
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers 按 非递减顺序 排列
-1000 <= target <= 1000
仅存在一个有效答案

"""

"""
解题思路：
# 采用双指针的思路来思考下：
# 数组是个升序排序的数组
# 左指针 left 指向数组开始位置
# 右指针 right 指向数组结束位置

# 则 我们判断 nums[left]+nums[right] 的值是否等于 target
# 1. 若不等，如果和小于 target: 则 left 指针左移
# 2. 若不等，如果和大于 target: 则 right 指针右移
# 最后， left !=right, 因为题目里要求不能使用重复的元素
"""

def f(nums, target):
	left, right = 0, len(nums)-1

	while left < right:
		sums = nums[left]+nums[right]
		if sums == target:
			return left+1, right+1
		elif sums > target:
			right -= 1
		else:
			left += 1



if __name__ == "__main__":
	print(f([2, 7, 11, 15], 9)) # (1, 2)
	print(f([2, 3, 4], 6))  # (1, 3)
	print(f([-1, 0], -1))  # (1, 2)