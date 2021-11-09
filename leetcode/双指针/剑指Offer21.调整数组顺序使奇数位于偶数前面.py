# -*- coding: utf-8 -*-

"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


### 解题思路：
# 沿用双指针的思想，一个左指针，一个右指针。
# 左指针向右遍历，若是奇数就前移一位；右指针往左遍历，若是偶数就前移一位
# 若是左指针是偶数，右指针是奇数，两个位置的值交换


def exchange(nums):
	left, right = 0, len(nums)-1

	while left < right:
		if nums[left] % 2 == 1:
			left += 1
		else:
			if nums[right] % 2 == 1:
				tmp = nums[left]
				nums[left] = nums[right]
				nums[right] = tmp
			else:
				right -= 1

	return nums


if __name__ == "__main__":
	nums = [1, 2, 3, 4]
	print(exchange(nums))  