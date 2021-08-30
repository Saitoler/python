# -*- coding: utf-8 -*- 

# 冒泡排序
# 思路就是像吹泡泡一样，上者为重，下者为轻
# 每一次将两个相邻的数字相比较，大的移动到右侧， 然后再与下一个数比较，直到数组尾
#  - 为什么到 len(nums)-1 就停了？ 因为最终最后一位一定是那个最大的数，不需要再
#    进行对比（内层循环里是和 j+1 对比的）
#  - 内层循环的边界是 len(nums)-1-i 的原因是： i 相当于是已处理的元素个数 
#    第一轮，已处理是0，那内层循环就是 len(nums)-1，每外层循环一次，相当于已处理完
#    一个元素，那就少处理一个

# 最优时间复杂度： 当所有的元素都已升序排列时，只要遍历一遍即可结束，此时复杂度为 O(N^2)
# 最差时间复杂度： 当所有的元素都是降序排列时，内外循环都要跑一遍，时间复杂度为 O(n^2)

def bubbleSort(nums):
	for i in range(len(nums)-1):
		for j in range(len(nums)-1-i):
			if nums[j] > nums[j+1]:
				temp = nums[j]
				nums[j] = nums[j+1]
				nums[j+1] = temp
			j += 1
		i += 1

	return nums


if __name__ == "__main__":
	nums = [1, 4, 2, 3, 6, 5, 7]
	print(bubbleSort(nums))

