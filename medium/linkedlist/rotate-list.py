# name: 61. rotate list
# link: https://leetcode.com/problems/rotate-list

# solution #
class Solution:
	def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		# no need to rotate
		if k == 0 or not head:
			return head
		
		count, curr = 0, head
		
		# count the number of nodes
		while curr:
			count += 1
			curr = curr.next
		
		# number of rotations
		rem = k % count
		
		# k is the same size as the list; no rotations needed
		if rem == 0:
			return head
		
		prev = head
		curr = prev
		
		# count - rem - 1 means we start from the front
		for _ in range(count - rem - 1):
			curr = curr.next
		
		# new head, set new tail.next to None
		head = curr.next
		curr.next = None
		
		curr = head
		
		# while not at the end of new head list
		while curr.next:
			curr = curr.next
		
		# connect tail of new head to head of previous head
		curr.next = prev
		
		return head

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""