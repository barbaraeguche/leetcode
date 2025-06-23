# name: 791. custom sort string
# link: https://leetcode.com/problems/custom-sort-string

# solution #
class Solution:
	def customSortString(self, order: str, s: str) -> str:
		# use a hashmap
		count = Counter(s)
		string = ""
		
		for char in order:
			if char in count:
				ch, freq = char, count[char]
				
				# must appear all at once
				string += char * freq
				# delete from map as characters are unique
				del count[char]
		
		# add the rest that weren't present in order
		for char, freq in count.items():
			string += char * freq
		
		return string

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""