class ListNode(object):
    def __init__(self, val=0, n=None):
        self.val = val
        self.next = n


def merge_2_list(l1:ListNode, l2:ListNode):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val < l2.val:
        l1.next = merge_2_list(l1.next, l2)
        return l1
    else:
        l2.next = merge_2_list(l1, l2.next)
        return l2
