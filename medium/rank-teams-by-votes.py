# name: 1366. rank teams by votes
# link: https://leetcode.com/problems/rank-teams-by-votes

# solution #
class Solution:
	def rankTeams(self, votes: List[str]) -> str:
		num_teams = len(votes[0])
		count = defaultdict(List[int])
		
		for vote in votes:
			for idx, char in enumerate(vote):
				# for each character, keep track of position votes
				count.setdefault(char, [0] * num_teams)
				count[char][idx] -= 1
		
		# sort by position-idx, then alphabetically
		count = dict(sorted(count.items(), key=lambda x: (x[1], x[0])))
		
		return "".join(count.keys())
