# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        arr = []
        curr = self
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return " -> ".join(str(item) for item in arr)


def list_to_linkedlist(arr):
    if not arr:  # empty list
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        if head == None:
            return head

        curr = head

        while curr.next != None:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


sol = Solution()
listex = [1,1,2,3,3]
head = list_to_linkedlist(listex)
print(sol.deleteDuplicates(head))