l1 = [2,4,3]
l2 = [5,6,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        # Get values from nodes, or 0 if list is exhausted
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        
        # Create new node with the digit part
        current.next = ListNode(total % 10)
        
        # Move pointers forward
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        
    return dummy.next
# Helper function to convert list to linked list
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Convert lists to linked lists
l1_linked = list_to_linkedlist(l1)
l2_linked = list_to_linkedlist(l2)

# Call the function
result = addTwoNumbers(l1_linked, l2_linked)

# Convert result back to list and print
print(linkedlist_to_list(result))
