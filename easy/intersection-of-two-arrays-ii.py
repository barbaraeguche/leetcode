# name: 350. intersection of two arrays ii
# link: https://leetcode.com/problems/intersection-of-two-arrays-ii

# solution #
class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		nums1Map, nums2Map = defaultdict(int), defaultdict(int)
		intersection = []
		
		for num in nums1:
			nums1Map[num] += 1
		for num in nums2:
			nums2Map[num] += 1
		
		for k, v in nums1Map.items():
			if k in nums2Map:
				value = min(v, nums2Map[k])
				intersection.extend([k for _ in range(value)])
		
		return intersection

"""
time complexity:
- O(n + m)

space complexity:
- O(n + m)
"""