# name: 2807. insert greatest common divisors in linked list
# link: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list

# solution #
class Solution:
	def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if not head.next:
			return head
		
		prev, curr = head, head.next
		
		while curr:
			temp = math.gcd(prev.val, curr.val)
			node = ListNode(temp, curr)
			prev.next = node
			
			# update variables
			prev = curr
			curr = curr.next
		
		return head