# -*- coding: utf-8 -*-


"""
题目：
你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
图示两个链表在节点 c1 开始相交：
题目数据 保证 整个链式结构中不存在环。
注意，函数返回结果后，链表必须 保持其原始结构 。

 
示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。


示例 2：
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

"""


### 解题思路：
# 两个链表有相交， 则说明相交后的后续元素都是相同的
# 设， 链表 A 和链表 B，两者相交部分的长度为 c
# 链表 A 私有部分长度为 a
# 链表 B 私有部分长度为 b
# 则为了遍历链表A，元素个数为 a+c
# 为了遍历链表 B， 元素个数为 b+c
# 由此可看出两者长度不一定是相等的，如果是直接遍历，很难找到对应位置上的相交点
# 因为我们可以这样做：
# 设置两个指针，分别指向链表A，和链表B的开头
# 然后让两个指针，遍历完自己后，就指向另一个链表的表头，再遍历该链表，所以两个指针分别走过的个数为：
# nodeA 指针： a+c+b
# nodeB 指针： b+c+a
# 很明显 a+c+b = b+c+a
# 即两个指针走过的元素个数是相同的，故二者肯定会交汇在一点。
# 如果没有交汇点，则最终 nodeA、nodeB 均会走到链表结尾

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    
    nodeA, nodeB = headA, headB

    while nodeA != nodeB:
        if nodeA:
            nodeA = nodeA.next
        else:
            nodeA = headB
        
        if nodeB:
            nodeB = nodeB.next
        else:
            nodeB = headA
    
    return nodeA