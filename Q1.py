class ListNode:
def __init__(self, val=0, next=None):
self.val = val
self.next = next

def hasCycle(head):
if not head:
return False

slow = head # Slow pointer starts at the head.
fast = head # Fast pointer also starts at the head.
while fast and fast.next:
slow = slow.next # Move slow pointer one step.
fast = fast.next.next # Move fast pointer two steps.

if slow == fast: # If they meet, there is a cycle.
return True

# If fast pointer reaches the end, there is no cycle.
return False
