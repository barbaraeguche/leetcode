# name: 599. minimum index sum of two lists
# link: https://leetcode.com/problems/minimum-index-sum-of-two-lists

# solution #
class Solution:
	def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
		idx_sum = 999 + 999
		arr, l1 = [], [word for word in list1 if word in list2]
		
		for word in l1:
			# calculate the idx sum
			total = list1.index(word) + list2.index(word)
			
			# if the new sum is less than the prev sum
			if total < idx_sum:
				arr.clear()
				arr.append(word)
			
			# if the new sum is equal to the prev sum
			if total == idx_sum:
				arr.append(word)
			
			# update idx sum
			idx_sum = min(total, idx_sum)
		
		return arr
	