# -*- coding: utf-8 -*-

"""
题目：
给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

示例 1:
输入：s = "egg", t = "add"
输出：true

示例 2：
输入：s = "foo", t = "bar"
输出：false

示例 3：
输入：s = "paper", t = "title"
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/isomorphic-strings
"""

### 解题思路：
	# 满足如下条件：
	# 1. 每个出现的字符，都应当映射到另一个字符
	# 2. 不同的字符，不能映射到同一个字符上， 如 e--g,  a--g 这种是不允许的
	# 3. 相同的字符，只能映射到同一个字符上， 如 e--g,  e--h 这种是不允许的
	# 4. 字符可以映射到本身
# 翻译到代码中的判断：
# 1. 已经在前面出现过的字符映射关系，对于同一个 s[i]， 不能映射到其他字符上去
#    即 s[i] = t[i], 不能再出现一个 s[i+1]=s[i] 时， t[i]!=s[i+1]
# 2. 前面未出现过的 s[i]， 其对应的 t[i] 不能是已经出现在前面的映射关系中了，否则就
#    不满足上面的条件2了
# 从映射关系上已经可以很明显的看出这道题要使用 dict 来作为 hash 表了。


def isIsomorphic(s, t):
    hashtable = {}

    for i in range(len(s)):
        if s[i] in hashtable:
            if hashtable[s[i]] != t[i]:
                return False
        else:
            if t[i] in hashtable.values():
                return False
            else:
                hashtable[s[i]] = t[i]
    
    return  True


if __name__ == "__main__":
	s1 = "egg"
	t1 = "add"

	s2 = 'foo'
	t2 = 'bar'

	s3 = 'paper'
	t3 = 'title'

	s4 = 'badc'
	t4 = 'baba'

	s5 = 'aaeaa'
	t5 = 'uuxyy'

	print(isIsomorphic(s1, t1))
	print(isIsomorphic(s2, t2))
	print(isIsomorphic(s3, t3))
	print(isIsomorphic(s4, t4))
	print(isIsomorphic(s5, t5))
