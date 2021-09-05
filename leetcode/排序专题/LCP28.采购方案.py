# -*- coding: utf-8 -*-

"""
题目：

小力将 N 个零件的报价存于数组 nums。小力预算为 target，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。
注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1

示例 1：
输入：nums = [2,5,3,5], target = 6
输出：1
解释：预算内仅能购买 nums[0] 与 nums[2]。

示例 2：
输入：nums = [2,2,1,9], target = 10
输出：4
解释：符合预算的采购方案如下：
nums[0] + nums[1] = 4
nums[0] + nums[2] = 3
nums[1] + nums[2] = 3
nums[2] + nums[3] = 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4xy4Wx
"""

### 解题思路
# 和LCP18一样的思路，使用双指针的方式，来降低时间复杂度
# 这道题其实思路是一样的，最重要的是，要找出 count 值怎么计算
# 在这道题中，count 应该是从(j-i)中得到的，可以自己遍历下算几次就知道了。

    # 买两个零件，花费不超过预算，即 nums[i]+nums[j] <= target 为满足条件的

    # 设 count 为采购方案数量
    # 设 i 为零件1的下标， 设 j 为零件2的下标
    # 则根据题意有：
    # 1. i != j   同样的零件不能买两个
    # 2. nums[i]+nums[j] <= target

    # 还是同样的排序思路，对数组 nums 排序，排序后有 nums[i] <= nums[i+1]
    # 定义两个指针， i指向数组开头， j 指向数组结尾
    # 如果 满足条件，即 nums[i]+nums[j] <= target, 则当前 i 的情况下，共有 j-i 种组合 --这个太重要了！！！！
    # 
    # 如果不满足该条件， 则将 j 前移一位，找较小的数据再尝试

def purchasePlans(nums, target):
    # 先排序
    nums.sort()

    # 声明前后指针，定义解决方案个数
    count, i, j = 0, 0, len(nums)-1

    # j>i是为了防止二次查找
    while i<len(nums) and j>i:
        if nums[i]+nums[j] <= target:
            # j-i 就是当前i下的解决方案个数
            count += (j-i)
            # 前指针加1
            i += 1
        else:
            # 后指针后移
            j -= 1

    return count


if __name__ == "__main__":
    nums1, target1 = [2, 5, 3, 5], 6
    nums2, target2 = [2, 2, 1, 9], 10

    print(purchasePlans(nums1, target1))
    print(purchasePlans(nums2, target2))
