# name: 23. merge k sorted lists
# link: https://leetcode.com/problems/merge-k-sorted-lists

# solution #
import heapq as hq

class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		if not lists:
			return None
		
		minHeap = []
		
		for i, node in enumerate(lists):
			if node:
				hq.heappush(minHeap, (node.val, i, node))
		
		head = ListNode(-1)
		curr = head
		
		while minHeap:
			val, i, node = hq.heappop(minHeap)
			
			curr.next = node
			curr = curr.next
			node = node.next
			
			if node:
				hq.heappush(minHeap, (node.val, i, node))
		
		return head.next
	
"""
time complexity:
- O(n * log(k)); n is the total number of nodes across k lists, k is the length of the list

space complexity:
- O(k)
"""