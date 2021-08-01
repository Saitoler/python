# -*- coding: utf-8 -*-

"""
题目：

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 
示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""

### 解题思路：
### 先分析下题目 -
###  1. 买入的时间，必须在卖出之前，如果用两个指针来记录，即 buy < sell
###  2. 卖出的价格，必须大于买入的价格， 即 prices[buy] < prices[sell], 则 prices[sell]-prices[buy] > 0 才是真正能卖出的组合
#   这道题就很像之前求最大连续子序列和的问题， 不同的是，这道题里的不是最大连续子序列之和，而是非连续序列的首尾差
#  
def maxProfit(prices):
    maxi = 0

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if j > i and prices[j] > prices[i]:
                maxi = max(maxi, prices[j]-prices[i])

    return maxi


### 上面那种方式在 python 里面会运行超时……，所以还是要想其他办法来解决：
### 换种思路， 是否有遍历一遍数组就能解决的方法呢？
### 1. 我们预设最大利润是 maxi = 0, 这样如果出现没有利润时，也能直接返回 maxi 
### 2. 预设一个最小价格为 mini = prices[0]
### 3. 从第二个值开始遍历数组一遍， 每个遍历中，更新下最小价格 mini, 取一个最小价格来
### 4. 每个遍历中，同时算一下当前价格与最小价格的差值，更新 maxi

def maxProfit2(prices):
    maxi = 0
    mini = prices[0]

    for i in range(1, len(prices)):
        mini = min(mini, prices[i])
        maxi = max(maxi, prices[i]-mini)
    
    return maxi

if __name__ == "__main__":
    nums1 = [7,1,5,3,6,4]
    nums2 = [7,6,4,3,1]
    

    print(maxProfit2(nums1))
    print(maxProfit2(nums2))
