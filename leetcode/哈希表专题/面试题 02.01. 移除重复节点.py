# -*- coding: utf-8 -*-

"""
题目：
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:
 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]

示例2:
 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]


提示：
链表长度在[0, 20000]范围内。
链表元素在[0, 20000]范围内。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-node-lcci
"""

### 解题思路： 属于链表的操作，要学会使用 python 来进行链表数据结构题目的处理
### 使用一个数组来存储已访问过的节点，如果再次访问到该节点，就跳过，将链表的下一跳，指向后面的节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def removeDuplicateNodes(head):
    if not head:
        return head
    
    visited = [head.val]
    pos = head

    while pos.next:
        curr = pos.next
        if curr.val not in visited:
            visited.append(curr.val)
            pos = pos.next
        else:
            pos.next = pos.next.next
        
    return head
