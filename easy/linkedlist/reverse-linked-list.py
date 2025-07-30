# name: 206. reverse-linked-list
# link: https://leetcode.com/problems/reverse-linked-list

# solution #
class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		prev, curr = None, head
		
		while curr:
			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp
		
		return prev
	