# name: 451. sort characters by frequency
# link: https://leetcode.com/problems/sort-characters-by-frequency

# solution #
class Solution:
	def frequencySort(self, s: str) -> str:
		string = ""
		counter = Counter(s)
		
		for tup in counter.most_common():
			char, num = tup
			
			# append char * num
			string += f"{char * num}"
		
		return string
	