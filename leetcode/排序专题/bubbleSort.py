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
		print("中间过程中 nums 为", nums)

	return nums






# 按照上面的代码，如果数组已经是排好序的，是否会有重复的步骤呢？我们以 nums2 = [1, 1, 2, 3, 4, 5]来跑一遍，结果如下
# 中间过程中 nums 为 [1, 1, 2, 3, 4, 5]
# 中间过程中 nums 为 [1, 1, 2, 3, 4, 5]
# 中间过程中 nums 为 [1, 1, 2, 3, 4, 5]
# 中间过程中 nums 为 [1, 1, 2, 3, 4, 5]
# 中间过程中 nums 为 [1, 1, 2, 3, 4, 5]
# [1, 1, 2, 3, 4, 5]


# 如上，可以看到，即使已经是排好序的数组了，代码还是会跑 n-1遍，这里是5遍。
# 那怎么优化呢？
# 我们可以设立一个标记位 flag，  设为 FALSE
# 在内部循环的元素交换后，为这个 flag 赋值，即有元素交换的话， 就重置这个 flag, 那当flag 没有被重置时，就说明一个完整的一轮
# 比较中都没有交换元素，说明数组已经是排序好了的，就直接退出循环即可
# 代码如下：

def bubbleSort2(nums):
	# 设置标记位为 False
	flag = False

	for i in range(len(nums)-1):
		for j in range(len(nums)-i-1):
			if nums[j] > nums[j+1]:
				tmp = nums[j]
				nums[j] = nums[j+1]
				nums[j+1] = tmp 
				flag = True
		print("中间过程中 nums 为", nums)
		# 如果flag 依旧是 False, 说明内部循环中没有进行过元素交换，数组已经是排序好了的。
		if not flag:
			break

	return nums


if __name__ == "__main__":
	nums = [1, 1, 2, 3, 4, 5]
	print(bubbleSort(nums))

	print(bubbleSort2(nums)) 
	# 执行后的结果： 
	#    中间过程中 nums 为 [1, 1, 2, 3, 4, 5]
	#    [1, 1, 2, 3, 4, 5]

