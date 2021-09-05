# -*- coding: utf-8 -*-

"""
题目：
小扣在秋日市集选择了一家早餐摊位，一维整型数组 staple 中记录了每种主食的价格，一维整型数组 drinks 中记录了每种饮料的价格。小扣的计划选择一份主食和一款饮料，且花费不超过 x 元。请返回小扣共有多少种购买方案。
注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1

示例 1：
输入：staple = [10,20,5], drinks = [5,5,2], x = 15
输出：6
解释：小扣有 6 种购买方案，所选主食与所选饮料在数组中对应的下标分别是：
第 1 种方案：staple[0] + drinks[0] = 10 + 5 = 15；
第 2 种方案：staple[0] + drinks[1] = 10 + 5 = 15；
第 3 种方案：staple[0] + drinks[2] = 10 + 2 = 12；
第 4 种方案：staple[2] + drinks[0] = 5 + 5 = 10；
第 5 种方案：staple[2] + drinks[1] = 5 + 5 = 10；
第 6 种方案：staple[2] + drinks[2] = 5 + 2 = 7。

示例 2：
输入：staple = [2,1,1], drinks = [8,9,5,1], x = 9
输出：8

解释：小扣有 8 种购买方案，所选主食与所选饮料在数组中对应的下标分别是：
第 1 种方案：staple[0] + drinks[2] = 2 + 5 = 7；
第 2 种方案：staple[0] + drinks[3] = 2 + 1 = 3；
第 3 种方案：staple[1] + drinks[0] = 1 + 8 = 9；
第 4 种方案：staple[1] + drinks[2] = 1 + 5 = 6；
第 5 种方案：staple[1] + drinks[3] = 1 + 1 = 2；
第 6 种方案：staple[2] + drinks[0] = 1 + 8 = 9；
第 7 种方案：staple[2] + drinks[2] = 1 + 5 = 6；
第 8 种方案：staple[2] + drinks[3] = 1 + 1 = 2；



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/2vYnGI

"""

### 第一想法就是直接爆破遍历两边数组即可……然而这样肯定会超时

def breakfastNumber1(staple, drinks, x):
    count = 0
    for i in range(len(staple)):
        for j in range(len(drinks)):
            if (staple[i]+drinks[j]) <= x:
                count += 1
    
    return count

### 于是就要想办法去优化。。
## 看了题解里的思路，基本都是利用 排序+双指针 来降低复杂度，具体思路是
# 这道题本质上就是要找出满足 staple[i]+drinks[j] <= x 的有效组合
# 如果对两个数组先进行升序排序，则就有：
# staple[i] <= staple[i+1]...
# drinks[j] <= drinks[j+1]...
# 因此我们可以设置两个指针，一个 i 指向 staple 数组的开头
# 另一个 j 指向 drinks 数组的结尾
# 这样有什么用呢？
#   - 因为 j 指向结尾，一旦满足 staple[i]+drinks[j] <= x， 那么 staple[i]+drinks[j-1] 的所有元素也都满足
#   - 这种情况直接计算当前 i 的条件下的满足数量即可，J 的值不动，保持原位
#   - 如果不满足 staple[i]+drinks[j] <= x， 那就将 j 向前移一位，找一个较小的元素尝试，直到 drinks 的开头位置，如果还
#   - 不满足的话，则直接退出，因为 staple[i]+drinks[j] > x 的话
#   - 就一定有 staple[i+1]+drinks[j] > x

# 基于上述想法，代码如下：

def breakfastNumber2(staple, drinks, x):
    # 先对两个数组进行排序
    staple.sort()
    drinks.sort()

    # 定义前后指针，结果总数
    count, i, j = 0, 0, len(drinks)-1

    while i<len(staple) and j >= 0:
        if staple[i]+drinks[j] <= x:
            # 符合条件，j 的下标值加1，就是当前符合条件的drinks 个数
            count += j+1
            # 直接将 i 递增，继续下一次，因为当前已经无需再运算了
            i+= 1
        else:
            # 不符合条件，就把 j 递减一位，找一个小数据再尝试匹配
            j -= 1
    
    return count


if __name__ == "__main__":
    staple = [10, 20, 5]
    drinks = [5, 5, 2]
    x = 15

    print(breakfastNumber1(staple, drinks, x))
    print(breakfastNumber2(staple, drinks, x))
    