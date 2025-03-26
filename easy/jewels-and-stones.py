# name: 771. jewels and stones
# link: https://leetcode.com/problems/jewels-and-stones

# solution #
class Solution:
	def numJewelsInStones(self, jewels: str, stones: str) -> int:
		return sum(stones.count(st) for st in set(stones) if st in jewels)