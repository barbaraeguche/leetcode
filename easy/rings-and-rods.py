# name: 2103. rings and rods
# link: https://leetcode.com/problems/rings-and-rods

# solution #
class Solution:
	def countPoints(self, rings: str) -> int:
		rr_dict: Dict[str, List[str]] = {}
		splitted = [rings[k:k+2] for k in range(0, len(rings), 2)]
		
		for rr in splitted:
			rr_dict.setdefault(rr[-1], []).append(rr)
		
		total = [k for k,v in rr_dict.items() if len(set(v)) == 3]
		return len(total)