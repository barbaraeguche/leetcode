# name: 3217. delete nodes from linked list present in array
# link: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array

# solution #
class Solution:
	def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
		nums = set(nums)
		current = head
		
		while current and current.next:
			while current.next and current.next.val in nums:
				current.next = current.next.next
			
			current = current.next
		
		if head and head.val in nums:
			head = head.next
		
		return head
	