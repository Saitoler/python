# -*- coding: utf-8

"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：
2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案

链接：https://leetcode-cn.com/problems/two-sum
"""



"""
# 解法1:
# 最先想到的方法，x+y=target, 那么 y=target-x
# 只要判断 y 是否在数组中即可。故使用两层循环：
#     第一层循环，从第一个数开始遍历数组
#     第二层循环，从下一个数开始，逐个确认是否为 y
# 这种解法的时间复杂度为 O(n^2)
"""

def twoSum(nums, target):
    for i in range(0, len(nums)):
        if(target-nums[i]) in nums:
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


"""
# 解法2：
# 思路同解法1， y=target-x,同样也是要搜索是否存在 y 在数组中
# 但换个思路，从 dict 中进行查找，因为 dict 中 可以直接保存数据的值和下标
# 可以通过 enumerate() 方法，将原数组中的数据，按照[值，下标]方式存入 dict
#    查询 y 是否存在于 dict：
#       若存在，则返回 [dict[y], i]
#       若不存在，将当前的  x  写入 dict 中，以数组中的值作为 key, 以对应的下标作为 value
#    后面查询 y 是否在，直接通过  y in dict.keys() 即可知道。
"""

def twoSum2(nums, target):
    hashtable = dict()

    # enumerate() 接口，可以将 list, tuple等的数据按 下标-元素 的形式对应起来。
    # for k,v in enumerate(nums):
    #     print(k, v)
        # 0 2
        # 1 7
        # 2 11
    
    for i, num in enumerate(nums):
        if (target-num) in hashtable.keys():
            return [hashtable[target-num], i]
        else:
            hashtable[num] = i


    

#   测试代码 

if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    target1 = 9

    nums2 = [3, 2, 4]
    target2 =  6

    print(twoSum(nums1, target1)) # [0, 1]
    print(twoSum(nums2, target2)) # [1, 2]

    print(twoSum2(nums1, target1))
    print(twoSum2(nums2, target2))