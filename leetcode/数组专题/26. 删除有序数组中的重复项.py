# -*- coding: utf-8 -*-


"""
题目：

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


示例 1：

输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
"""


### 解题思路
# 有时候写代码前将可能的测试集列出来，想一想就可以知道怎么操作了，声明两个指针，作为基准对比
# 步骤如下：
# 1.  从第二个数字开始，以第一个数字为基准，由于是升序排列的有序数组，所以直接判断第二个数是否大于第一个数 
# 2.  若大于，则表明这两个数，不存在相同的，将两个要比较的指针都往前前进一位进行下一波循环
# 3.  若不大于，则肯定是等于的，就将第一个数直接 pop 掉，数组中就少了一个重复元素，重制指针，从开头重新进行下一波匹配


def removeDuplicates(nums):
    base, current = 0, 1

    while current < len(nums):
        if nums[current] > nums[base]:
            current += 1
            base += 1
        else:
            nums.pop(base)
            base, current = 0, 1

    return len(nums)


### 关于是否原地解决的说明：
# 一直在怀疑自己使用 pop 函数后的数组是新的引用还是原引用，所以这里做了个小实验：
# 如下， 对 pop  前后的数组 分别使用  id() 方法 ，结果表明，并没有新的空间占用，
# 两者引用的是同一个对象
# nums = [1, 2, 4, 6]
# print(id(nums)) #4396776576
# nums.pop(0)
# print(id(nums)) #4396776576


if __name__ == "__main__":
    nums1 = [0,0,1,1,1,2,2,3,3,4]
    nums2 = [1, 1, 2, 2, 2, 3, 3]
    nums3 = [1, 2, 3, 4]
    print(removeDuplicates(nums1))
    print(removeDuplicates(nums2))
    print(removeDuplicates(nums3))
