# name: 819. most common word
# link: https://leetcode.com/problems/most-common-word

# solution #
class Solution:
	def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
		filtered = re.sub(r'[^a-zA-Z\s]', ' ', paragraph).lower().split()
		not_banned = [word for word in filtered if word not in banned]
		
		counter = Counter(not_banned)
		return counter.most_common()[0][0]