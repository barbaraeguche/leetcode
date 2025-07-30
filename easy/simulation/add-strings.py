# name: 415. add strings
# link: https://leetcode.com/problems/add-strings

# solution #
class Solution:
	def addStrings(self, num1: str, num2: str) -> str:
		base, queue = ord('0'), deque()
		
		def addNums(i: int, j: int, carry: int) -> str:
			if i < 0 and j < 0 and carry == 0:
				return None
			
			n1 = num1[i] if i >= 0 else "0"
			n2 = num2[j] if j >= 0 else "0"
			
			# summation of all three numbers
			summation = (ord(n1) - base) + (ord(n2) - base) + carry
			carry, value = divmod(summation, 10)
			
			# store in queue
			queue.appendleft(value)
			
			# perform recursion till last number
			return addNums(i - 1, j - 1, carry)
		
		# perform the addition
		addNums(len(num1) - 1, len(num2) - 1, 0)
		
		return "".join(str(num) for num in queue)

"""
time complexity:
- O(max(n, m)); n is the length of num1, m is the length of num2

space complexity:
- O(max(n, m))
"""