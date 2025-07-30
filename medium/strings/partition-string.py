# name: 3597. partition string
# link: https://leetcode.com/problems/partition-string

# solution #
class Solution:
	def partitionString(self, s: str) -> List[str]:
		idx, length = 0, len(s)
		
		seen = set()
		string, partitions = "", []
		
		while idx < length:
			string += s[idx]
			
			if string in seen:
				idx += 1
				continue
			
			# add current segment to set
			seen.add(string)
			# add current segment to partitions
			partitions.append(string)
			
			# reset variables
			idx, string = idx + 1, ""
		
		return partitions

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""