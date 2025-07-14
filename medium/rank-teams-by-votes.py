# name: 1366. rank teams by votes
# link: https://leetcode.com/problems/rank-teams-by-votes

# solution #
class Solution:
	def rankTeams(self, votes: List[str]) -> str:
		teams = len(votes[0])
		count = defaultdict(lambda: [0] * teams)
		
		for vote in votes:
			# for each character, keep track of the position
			for idx, char in enumerate(vote):
				count[char][idx] -= 1
		
		# sort by position-idx, then alphabetically
		count = dict(sorted(count.items(), key=lambda x: (x[1], x[0])))
		
		return "".join(count.keys())

"""
time complexity:
- O(n * m * log(m)); n is the length of votes, m is the average word length

space complexity:
- O(n * m)
"""