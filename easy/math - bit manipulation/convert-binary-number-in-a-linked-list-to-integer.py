# name: 1290. convert binary number in a linked list to integer
# link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

# solution #
class Solution:
	def getDecimalValue(self, head: Optional[ListNode]) -> int:
		number = 0
		
		while head:
			number = (number << 1) | head.val
			head = head.next
		
		return number


"""
time complexity:
- O(n)

space complexity:
- O(1)
"""