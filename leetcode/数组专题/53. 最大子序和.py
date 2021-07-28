# -*- coding: utf-8 -*-

"""
题目：
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
"""


### 解题思路：
### 采用动态规划的思想来思考这道题：
# 以 nums = [-1, 2, 4, -3, 1]为例：
# 最长 连续公共子序列的开始状态就是第一个元素，我们可以新开一个数组来记录最大公共子序列之和
# 那么，初始状态下，    sum[0] = nums[0] = -1
# ### 下一步的递推条件，sum[n] = sum[n-1]+nums[n], 即用之前记录下来的 sum,加上当前的值
# ### 这个时候就有两种情况：
# ### 1. sum[n-1]+nums[n] > nums[n] -- 表明之前的子序列加上当前值，是对最大子序列这个目标有用的‘
# ### 2. sum[n-1]+nums[n] < nums[n] -- 表明前面的字串对于求最大公共字串无用，
# ### 所以最终得出推导结论：
# ###  - 对于 case1, 则将 nums[n] 加入最长公共字串，将sum[n]更新为 sum[n-1]+nums[n]
# ###  - 对于 case2, 则将 sum[n-1] 丢弃，直接从 nums[n] 开始重新计算子序列，sum[n] 被更新为 nums[n]
# ###  最终返回 sum[n] 即可。
# 代码如下：
 

def maxSubArray(nums):
    sum = nums[0]
    maxi = nums[0]

    for i in range(1, len(nums)):
        sum = max(sum+nums[i], nums[i])
        if sum >= maxi:
            maxi = sum
    
    return maxi



if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


