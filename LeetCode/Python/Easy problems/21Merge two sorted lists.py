from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, listOne: ListNode, listTwo: ListNode) -> ListNode:
        mergedHead = ListNode()
        current = mergedHead

        while listOne and listTwo:
            if listOne.val < listTwo.val:
                current.next = listOne
                listOne = listOne.next
            else:
                current.next = listTwo
                listTwo = listTwo.next
            current = current.next

        current.next = listOne if listOne else listTwo
        return mergedHead.next
