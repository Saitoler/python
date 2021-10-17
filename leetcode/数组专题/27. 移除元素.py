# -*- coding: utf-8 -*-

"""
题目：

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
"""


### 解题思路：
# 相对简单， 我们只需要来遍历数组，对于不是目标 val 的元素进行计数，

def removeElement(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    
    return count

# 上面的解法只能说是钻题目漏洞，根本不算是解决了这道题
# 这道题和26题类似，可以使用双指针的解法来进行解题
# 定义双指针 slow, fast， 初始值都设置为0，
# slow 指向的是不包含 val 的区间的末尾，fast 则在前面搜索 val, 如果是 val,就用后面的元素覆盖他

def removeElement2(nums, val):
    slow, fast = 0, 0

    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

        fast += 1
    return slow


# 上面的双指针解法在 val 值较少时，有可能会导致重复搬运无需处理的元素，例如 [1, 2, 3, 4, 5]， val=1
# 按照上面的双指针解法，要把后面的值依次向前搬一次，而事实上，直接将末尾的5覆盖到第一位即可
# 所以如下的双指针，左指针指向数组开始，右指针指向数组末尾
# 判断左指针指向的元素是否是 val, 如果是，就将末尾的值覆盖过来，然后将右指针左移一位
# 此时若覆盖过来的元素还是等于 val，就继续将右指针指向的值搬过来，一直重复这个步骤
# 如果左指针指向的元素不是 val, 就将左指针右移一次

# 这样遍历一遍，直到left 和right 相遇，[0,left) 区间内都没有 val 值 

def removeElement3(nums, val):
    left, right = 0, len(nums)-1

    while left <= right:
        if nums[left] == val:
            nums[left] = nums[right]
            right -= 1
        else:
            left += 1

    return left

if __name__ == "__main__":
    print(removeElement([3,2,2,3], 3))
    print(removeElement([0,1,2,2,3,0,4,2], 2))

    print(removeElement2([3,2,2,3], 3))
    print(removeElement2([0,1,2,2,3,0,4,2], 2))

    print(removeElement3([3,2,2,3], 3))
    print(removeElement3([0,1,2,2,3,0,4,2], 2))

