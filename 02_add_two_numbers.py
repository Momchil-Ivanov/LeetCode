# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
         # Convert linked lists to regular lists
        def list_to_array(head):
            result = []
            current = head
            while current:
                result.append(current.val)
                current = current.next
            return result
        
        # Get arrays from linked lists
        arr1 = list_to_array(l1)
        arr2 = list_to_array(l2)
        
        # Convert to numbers (reverse order as per problem)
        num1 = int(''.join(map(str, arr1[::-1])))
        num2 = int(''.join(map(str, arr2[::-1])))
        
        # Add numbers
        total = num1 + num2
        
        # Convert back to reversed array
        result_str = str(total)[::-1]
        result_arr = [int(digit) for digit in result_str]
        
        # Convert array back to linked list
        if not result_arr:
            return None
        
        head = ListNode(result_arr[0])
        current = head
        for digit in result_arr[1:]:
            current.next = ListNode(digit)
            current = current.next
        
        return head


# Test
if __name__ == "__main__":
    # Create test linked lists
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    
    # Convert result back to list for display
    def linked_list_to_list(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    print(f"Input: [2,4,3] + [5,6,4]")
    print(f"Output: {linked_list_to_list(result)}")
    print(f"Expected: [7,0,8]")
