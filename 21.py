def mergeTwoLists(list1, list2):
    if not (list1 and list2):
        return list1 or list2

    if list1.val >= list2.val:
        return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))

    return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))



def mergeIteratively(l1, l2):
    dummy = cur = ListNode()

    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    cur.next = l1 or l2
    return dummy.next