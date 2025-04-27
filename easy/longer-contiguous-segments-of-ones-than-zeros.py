# name: 1869. longer contiguous segments of ones than zeros
# link: https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros

# solution #
class Solution:
	def checkZeroOnes(self, s: str) -> bool:
		def remove_empty(arr: List[str]):
			return ' '.join(arr).split()
		
		zeros, ones = remove_empty(s.split('1')), remove_empty(s.split('0'))
		
		max_zeros = zeros if len(zeros) == 0 else max(zeros, key=len)
		max_ones = ones if len(ones) == 0 else max(ones, key=len)
		
		return len(max_zeros) < len(max_ones)
	