# -*- coding: utf-8 -*-

"""
题目：

给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate
"""

### 解题思路：
### 这道题用python 的方式去解会非常简单，来看下如何解决：
###    - 使用 set 不会有重复元素的特性， 直接对比两者的长度， 即可找出是否有重复元素

def containsDuplicate(nums):
    if len(nums) != len(set(nums)):
        return True
    return False
    # 进一步，可以简化成一行代码：
    #return len(nums) != len(set(nums))

### 还有其他的思路，可以使用哈希表 - 在 python 里，即使用字典，遍历数组将元素放入字典中，如果后面遍历发现该元素已经存在了，说明有重复的元素
### 如下的代码，在实际执行过程中会超时…  虽然实在没搞懂因为什么。
def containsDuplicate2(nums):
    hashtable = dict()

    for i in range(len(nums)):
        if nums[i] in hashtable.values():
            return True
        else:
            hashtable[i] = nums[i]
    
    return False

# 将上面的代码稍微改下，改成这个样子就不会超时了…… 没搞懂为什么遍历  values 会超时

def containsDuplicate3(nums):
    hashtable = dict()

    for i in range(len(nums)):
        if nums[i] in hashtable.keys():
            return True
        else:
            hashtable[nums[i]] = 0
    
    return False

if __name__ == "__main__":
    nums1 = [1,2,3,1]
    nums2 = [1,2,3,4]
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    print(containsDuplicate(nums1), containsDuplicate(nums2), containsDuplicate(nums3))
    print(containsDuplicate2(nums1), containsDuplicate2(nums2), containsDuplicate2(nums3))