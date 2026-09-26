# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        len_list = 0
        node = head
        while node:
            len_list+=1
            node = node.next
        
        # create first list
        l1_len = (len_list+1) // 2
        nodel1 = head

        for i in range(1, l1_len):
            nodel1 = nodel1.next

        # create second list
        nodel2 = nodel1.next
        nodel1.next = None

        prev = None
        for j in range(l1_len, len_list): # reverse l2
            tmp = nodel2.next
            nodel2.next = prev
            prev = nodel2
            nodel2 = tmp
        
        first, second = head, prev
        while second:
            print(type(first), type(second))
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

