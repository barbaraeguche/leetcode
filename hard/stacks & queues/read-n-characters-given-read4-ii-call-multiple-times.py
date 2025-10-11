# name: 158. read n characters given read4 ii call multiple times
# link: https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times

# solution #
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
	def __init__(self):
		self.buffer = deque([])
	
	def read(self, buf: List[str], n: int) -> int:
		i = 0
		
		while i < n:
			if self.buffer:
				buf[i] = self.buffer.popleft()
				i += 1
			else:
				temp = [""] * 4
				size = read4(temp)  # read the next 4 characters
				
				# end of file
				if not size:
					break
				
				for j in range(size):
					self.buffer.append(temp[j])
		
		return i

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""