# name: 2379. minimum recolors to get k consecutive black blocks
# link: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks

# solution #
class Solution:
	def minimumRecolors(self, blocks: str, k: int) -> int:
		count = 101  # max block len is 100
		
		for i, char in enumerate(blocks):
			seq = blocks[i:i+k]
			
			if len(seq) == k:
				count = min(count, seq.count('W'))
			
			# cannot be of length k, no need to go further
			else:
				break
		
		return count
