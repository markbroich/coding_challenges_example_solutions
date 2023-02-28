'''
234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a
palindrome or false otherwise.


Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head_node) -> bool:
        mid_node = self.__find_mid_and_end(head_node)
        end_node = self.__flip_next_pointer(mid_node)
        return self.__is_palidrone(head_node, end_node)

    def __find_mid_and_end(self, head_node):
        slow_pointer = head_node
        fast_pointer = head_node
        while fast_pointer.next:
            if fast_pointer.next:
                fast_pointer = fast_pointer.next
            if fast_pointer.next:
                fast_pointer = fast_pointer.next
                slow_pointer = slow_pointer.next
        return slow_pointer

    def __flip_next_pointer(self, mid_node):
        node = mid_node
        prior = None
        while node.next:
            next_node = node.next
            node.next = prior
            prior = node
            node = next_node
        node.next = prior
        return node

    def __is_palidrone(self, head_node, end_node):
        while head_node != end_node:
            if head_node.val != end_node.val:
                return False
            if not head_node.next:
                break
            head_node = head_node.next
            end_node = end_node.next
        return True


def tests():
    # head = [1,2,2,1]
    L1_head = ListNode(1)
    L1_head.next = ListNode(2)
    L1_head.next.next = ListNode(2)
    L1_head.next.next.next = ListNode(1)
    expected = True
    S1 = Solution()
    print(S1.isPalindrome(L1_head) == expected)

    # head = [1,2,3,4]
    L1_head = ListNode(1)
    L1_head.next = ListNode(2)
    L1_head.next.next = ListNode(3)
    L1_head.next.next.next = ListNode(4)
    expected = False
    S1 = Solution()
    print(S1.isPalindrome(L1_head) == expected)

    # head = [1,2,3,2,1]
    L1_head = ListNode(1)
    L1_head.next = ListNode(2)
    L1_head.next.next = ListNode(3)
    L1_head.next.next.next = ListNode(2)
    L1_head.next.next.next.next = ListNode(1)
    expected = True
    S1 = Solution()
    print(S1.isPalindrome(L1_head) == expected)

    # head = [1,2]
    L1_head = ListNode(1)
    L1_head.next = ListNode(2)
    expected = False
    print(S1.isPalindrome(L1_head) == expected)

    # head = [1,2,3,4,5]
    L1_head = ListNode(1)
    L1_head.next = ListNode(2)
    L1_head.next.next = ListNode(3)
    L1_head.next.next.next = ListNode(4)
    L1_head.next.next.next.next = ListNode(5)
    expected = False
    S1 = Solution()
    print(S1.isPalindrome(L1_head) == expected)

    # head = [1,2,3,9,1]
    L1_head = ListNode(1)
    L1_head.next = ListNode(2)
    L1_head.next.next = ListNode(3)
    L1_head.next.next.next = ListNode(9)
    L1_head.next.next.next.next = ListNode(1)
    expected = False
    S1 = Solution()
    print(S1.isPalindrome(L1_head) == expected)

    # head = [1,9,3,2,1]
    L1_head = ListNode(1)
    L1_head.next = ListNode(9)
    L1_head.next.next = ListNode(3)
    L1_head.next.next.next = ListNode(2)
    L1_head.next.next.next.next = ListNode(1)
    expected = False
    S1 = Solution()
    print(S1.isPalindrome(L1_head) == expected)


tests()








# def recursion(current_node = head):
#     if(current_node):
#         print(current_node.val)
#         if not recursion(current_node.next): return False
#         if(self.front_pointer.val != current_node.val): return False
#         self.front_pointer = self.front_pointer.next
#     return True
# return recursion()
