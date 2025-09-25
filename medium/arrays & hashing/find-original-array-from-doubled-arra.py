# name: 2007. find original array from doubled array
# link: https://leetcode.com/problems/find-original-array-from-doubled-array

# solution #
class Solution:
	def findOriginalArray(self, changed: List[int]) -> List[int]:
		changed.sort()  # sorting is a must
		
		# odd length; not possible
		if len(changed) % 2:
			return []
		
		original, countMap = [], defaultdict(int)
		
		# keep track of frequency
		for num in changed:
			countMap[num] += 1
		
		for num in changed:
			# previously removed; either as num or a multiple
			if num not in countMap or (num * 2) not in countMap:
				continue
			
			# for zero, the count needs to be even
			if num == 0 and countMap[num] % 2:
				return []
			
			# remove current num
			countMap[num] -= 1
			if countMap[num] == 0:
				del countMap[num]
			
			# remove doubled num
			countMap[num * 2] -= 1
			if countMap[num * 2] == 0:
				del countMap[num * 2]
			
			# note the original
			original.append(num)
		
		return original if not len(countMap) else []

"""
time complexity:
- O(n * log(n))

space complexity:
- O(n)
"""