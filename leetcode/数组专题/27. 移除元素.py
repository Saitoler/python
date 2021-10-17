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



if __name__ == "__main__":
    print(removeElement([3,2,2,3], 3))
    print(removeElement([0,1,2,2,3,0,4,2], 2))
