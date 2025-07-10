# name: 67. add binary
# link: https://leetcode.com/problems/add-binary

# solution #
class Solution:
	def addBinary(self, a: str, b: str) -> str:
		base, queue = ord('0'), deque()
		
		def addBin(i: int, j: int, carry: int) -> str:
			if i < 0 and j < 0 and carry == 0:
				return None
			
			n1 = a[i] if i >= 0 else "0"
			n2 = b[j] if j >= 0 else "0"
			
			# summation of all three numbers
			summation = (ord(n1) - base) + (ord(n2) - base) + carry
			carry, value = divmod(summation, 2)
			
			# store in queue
			queue.appendleft(value)
			
			# perform recursion till last number
			return addBin(i - 1, j - 1, carry)
		
		# perform the addition
		addBin(len(a) - 1, len(b) - 1, 0)
		
		return "".join(str(num) for num in queue)


"""
time complexity:
- O(max(n, m)); n is the length of a, m is the length of b

space complexity:
- O(max(n, m))
"""