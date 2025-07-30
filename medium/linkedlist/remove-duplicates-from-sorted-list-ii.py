# name: 82. remove duplicates from sorted list ii
# link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# solution #
class Solution:
	def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
		arr = []
		
		# add to array
		while head:
			arr.append(head.val)
			head = head.next
		
		# convert to counter
		counter = Counter(arr)
		arr = [k for k,v in counter.items() if v == 1]
		
		# if no non-duplicates
		if len(arr) == 0:
			return None
		
		head = ListNode(arr[0])
		curr = head
		
		# add single nums into new list
		for num in arr[1:]:
			curr.next = ListNode(num)
			curr = curr.next
		
		return head

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""