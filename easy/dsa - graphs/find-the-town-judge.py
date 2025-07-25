# name: 997. find the town judge
# link: https://leetcode.com/problems/find-the-town-judge

# solution #
class Solution:
	def findJudge(self, n: int, trust: List[List[int]]) -> int:
		adjacency = defaultdict(int)
		
		for src, dest in trust:
			adjacency[src] -= 1
			adjacency[dest] += 1
		
		for i in range(1, n + 1):
			if adjacency[i] == n - 1:
				return i
		
		return -1

"""
time complexity:
- O(v + e)

space complexity:
- O(v)
"""