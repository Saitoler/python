# -*- coding: utf-8 -*-

"""
给你一个整数数组 arr ，请你将数组中的每个元素替换为它们排序后的序号。
序号代表了一个元素有多大。序号编号的规则如下：
序号从 1 开始编号。
一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
每个数字的序号都应该尽可能地小。
 
示例 1：
输入：arr = [40,10,20,30]
输出：[4,1,2,3]
解释：40 是最大的元素。 10 是最小的元素。 20 是第二小的数字。 30 是第三小的数字。

示例 2：
输入：arr = [100,100,100]
输出：[1,1,1]
解释：所有元素有相同的序号

示例 3：
输入：arr = [37,12,28,9,100,56,80,5,12]
输出：[5,3,4,2,8,6,7,1,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rank-transform-of-an-array
"""

### 解题思路
# 要获取到序号，按题意即升序排列从1开始给每个元素编号，相同元素序号不增加
# 那么很明显就是要先对数组进行升序排序了，排序完成后再获取到元素和序号的对应关系即可

# 代码如下

def arrayRankTransform(arr):
    #先对空数组进行处理
    if not arr:
        return []
    
    ## 对数组进行排序
    sortedNums = sorted(arr)

    # 处理元素的序号
    # 初始序号是1，后面遇到相同的元素则序号不变，否则序号+1
    hashtable = {sortedNums[0]:1}
    index = 1

    for i in range(1, len(sortedNums)):
        if sortedNums[i] != sortedNums[i-1]:
            index += 1
        hashtable[sortedNums[i]] = index
    
    for i in range(len(arr)):
        arr[i] = hashtable[arr[i]]
    
    return arr


if __name__ == "__main__":
    arr = [40, 10, 20, 30]
    print(arrayRankTransform(arr))
    
