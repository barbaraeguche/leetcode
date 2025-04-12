# name: 884. uncommon words from two sentences
# link: https://leetcode.com/problems/uncommon-words-from-two-sentences

# solution #
class Solution:
	def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
		sp1 = s1.split()
		sp2 = s2.split()
		
		# find words not in the other
		l1 = [k for k,v in Counter(sp1).items() if v == 1 and k not in sp2]
		l2 = [k for k,v in Counter(sp2).items() if v == 1 and k not in sp1]
		
		return l1 + l2