class ListNode:
def __init__(self, val=0, next=None):
self.val = val
self.next = next

def detectCycle(head):
if not head or not head.next:
return None

slow = head
fast = head
# Step 1: Use Floyd's Cycle Detection to find the meeting point
while fast and fast.next:
slow = slow.next
fast = fast.next.next
if slow == fast:
break
# No cycle detected
if fast is None or fast.next is None:
return None

# Step 2: Find the start of the cycle
slow = head # Move slow pointer to the head
while slow != fast:
slow = slow.next
fast = fast.next

return slow # Both pointers are now at the start of the cycle
