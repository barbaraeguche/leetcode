# name: 234. palindrome linked list
# link: https://leetcode.com/problems/palindrome-linked-list

# solution #
class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		string = ""
		
		while head:
			string += str(head.val)
			head = head.next
		
		return string == string[::-1]
	