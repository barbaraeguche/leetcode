# name: 2326. spiral matrix iv
# link: https://leetcode.com/problems/spiral-matrix-iv

# solution #
class Solution:
	def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
		left, right = 0, n
		top, bottom = 0, m
		
		matrix = [[-1 for _ in range(n)] for _ in range(m)]
		
		while head:
			# row: left to right
			for i in range(left, right):
				if self.isEndOfList(head):
					break
				
				matrix[top][i] = head.val
				head = head.next
			top += 1
			
			# col: top to bottom
			for i in range(top, bottom):
				if self.isEndOfList(head):
					break
				
				matrix[i][right - 1] = head.val
				head = head.next
			right -= 1
			
			# row: right to left
			for i in range(right - 1, left - 1, -1):
				if self.isEndOfList(head):
					break
				
				matrix[bottom - 1][i] = head.val
				head = head.next
			bottom -= 1
			
			# col: bottom to top
			for i in range(bottom - 1, top - 1, -1):
				if self.isEndOfList(head):
					break
				
				matrix[i][left] = head.val
				head = head.next
			left += 1
		
		return matrix
	
	def isEndOfList(self, head: Optional[ListNode]) -> bool:
		return not head
