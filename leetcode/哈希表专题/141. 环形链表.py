# -*- coding: utf-8 -*-

"""
给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
""" 

### 解题思路：
# 这道题的题目让我看了半天看不懂……
# 主要的其实就是对这个 head 数据结构的理解：
# 从题干里的声明中可以看到：
#  head 是一个 ListNode 数据结构，含有两个属性：
#   - val:   表示值
#   - next:  指针，指向下一个 head 数据结构
#  - 遍历的时候其实就是修改 next 指针的值
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 如果遍历这个数组，从前往后依次访问每个元素，即依次修改 next 的值。
# 如果有元素在依次访问过程中被访问了两次，说明就有环～
# 可以将已遍历的元素放入 set 集合中，由于 set 是不会有重复元素的，所以
# 遍历过程中，一旦发现再次遍历的元素，在集合中能找到， 就说明有环。


def hasCycle(head):
    visited = set()

    for i in range(len(head)):
        if head[i] in visited:
            return True
        else:
            visited.add(head[i])
            head = head.next
    return False


