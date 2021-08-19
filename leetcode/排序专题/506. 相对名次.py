# -*- coding: utf-8 -*-

"""
题目：
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
(注：分数越高的选手，排名越靠前。)

示例 1:
输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。

提示:
N 是一个正整数并且不会超过 10000。
所有运动员的成绩都不相同。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-ranks
"""


### 解题思路：
# 思考过程如下：
# 1. 首先，要搞清楚数组中每个分数的对应名次
# 2. 然后，要将名次按照题目中要求的名次设定表示出来
# 3. 最后，就是要将原数组中的每个分数，替换成对应的名次设定值

# 对应名次等的首先想到的就是用 dict 来表示了
# 代码如下：

def findRelativeRanks(score):
    ## 先将名次设定生成：
    # 第一名记为 0

    # 前三名表示特殊，先单独生成
    rank = {
        0:'Gold medal',
        1:'Silver medal',
        2:'Bronze medal'
    }

    # 再对后续名次做设定：
    for i in range(3, 10000):
        rank[i] = str(i+1)
    
    score_rank = {}
    # 对原数组排序，用于获得每个分数对应的名次
    sorted_score = sorted(score, reverse=True)
    for i in range(len(sorted_score)):
        score_rank[sorted_score[i]] = i

    # 在原数组中，替换分数到相对名次里
    for i in range(len(score)):
        score[i] = rank[score_rank[score[i]]]
    
    return score


if __name__ == "__main__":
    score = [10,3,8,9,4]
    print(findRelativeRanks(score))  # ['Gold medal', '5', 'Bronze medal', 'Silver medal', '4']


