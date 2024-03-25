class ListNode:
def __init__(self, val=0, next=None):
self.val = val
self.next = next

def reverseList(head):
prev = None
current = head
while current:
next_temp = current.next # Step 3: Store the next node
current.next = prev # Reverse the current node's pointer
prev = current # Move prev forward
current = next_temp # Move current forward
return prev # At the end, prev is the new head of the reversed list
