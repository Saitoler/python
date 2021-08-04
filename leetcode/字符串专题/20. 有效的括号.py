# -*- coding: utf-8 -*-

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([)]"
输出：false

示例 5：
输入：s = "{[]}"
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
"""

### 解题思路：
### 根本没思路…… 
### 看了题解，这道题根本就是要使用栈这种数据结构， 要使用到栈的先进后出特性
### 具体思路就是：
### 因为括号要成对，肯定是一左一右，后面的右括号要在最近的地方找到对应的左括号
### 那么整体思路即： 遇到左括号，就压入栈中， 遇到右括号，就在栈顶检查该括号是否匹配，如果匹配，就弹出栈
###   如果都匹配，最后栈里面肯定是空的，若不是空栈，则表明不匹配
### 细分下来，具体有如下情况：
### 字符串为 "))"      -- 这种情况下没有左括号可以压栈的，因此栈也是空的，但却是不匹配的，所以应该返回 False
### 字符串为 "([}}])"  -- 这种情况下，压栈了前两个字符，中间有两个不匹配的，应该立即返回 False, 否则后面有两个刚好是和栈中的匹配的，就会弹栈称为空栈，导致判断错误

# 代码如下：
# 注： 其实本来可以用 switch case 来判断各种情况，将所有情况做一枚举。
#     但python 中没有 switch 语句， 故可以用 dict 来进行运算：


def isValid(s):
    if len(s) % 2 == 1:
        return False
    
    pairs = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    stack = []

    for c in s:
        if c in pairs:
            if not stack or pairs[c] != stack[-1]:
                return False
            stack.pop()
        else:
            stack.append(c)

    return not stack
        


if __name__ == "__main__":
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([)]"
    s5 = "{[]}"
    s6 = "){"
    s7 = "([}}])"
    s8 = "))"

    print(isValid(s1), isValid(s2), isValid(s3), isValid(s4), isValid(s5))
    print(isValid(s6))
    print(isValid(s7))
    print(isValid(s8))