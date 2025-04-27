# name: 2053. kth distinct string in an array
# link: https://leetcode.com/problems/kth-distinct-string-in-an-array

# solution #
class Solution:
	def kthDistinct(self, arr: List[str], k: int) -> str:
		distinct = [char for char in arr if arr.count(char) == 1]
		return "" if len(distinct) < k else distinct[k-1]
	