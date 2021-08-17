# -*- coding: utf-8 -*-
from functools import reduce
from collections import Counter


"""
题目：

给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

 

示例 1：
输入：["bella","label","roller"]
输出：["e","l","l"]

示例 2：
输入：["cool","lock","cook"]
输出：["c","o"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-common-characters
"""

### 解题思路：
#  这道题简直是为 Counter 量身打造的， 就是利用 Counter 的特性，对各个字符串进行计数
#  最后对得到的数据求交集，再返回所有的元素值即可。

## 知识点：
# 1. lambda 函数
# 2. map()
# 3. reduce()
# 4. Counter/Collections

def commonChars(words):
    return list(reduce(lambda x,y: x&y, map(Counter, words)).elements())
