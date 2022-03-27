class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add(l1, l2):
    result = trav = ListNode()
    carry = 0
    while l1 or l2 or carry:
        trav.next = ListNode()
        trav = trav.next
        trav.val += carry
        if l1:
            trav.val += l1.val
            l1 = l1.next
        if l2:
            trav.val += l2.val
            l2 = l2.next
        if trav.val > 9:
            carry = 1
            trav.val -= 10
        else:
            carry = 0

    return result.next


        
    