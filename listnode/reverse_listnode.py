# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 21:47
# @Author  : ziggy
# @File    : reverse_listnode.py
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        vals = [str(self.val)]
        nxt = self.next
        while nxt:
            vals.append(str(nxt.val))
            nxt = nxt.next
        return '->'.join(vals)


def reverse_list_node(head_node: ListNode):
    """ 反转链表 """
    if not head_node:
        return head_node

    new = None
    while head_node:
        tmp = head_node
        head_node = head_node.next
        tmp.next = new
        new = tmp
    return new


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(reverse_list_node(head))
