# name: 981. time based key-value store
# link: https://leetcode.com/problems/time-based-key-value-store

# solution #
class TimeMap:
	
	def __init__(self):
		self.timeMap = {}
	
	def set(self, key: str, value: str, timestamp: int) -> None:
		self.timeMap.setdefault(key, []).append((timestamp, value))
	
	def get(self, key: str, timestamp: int) -> str:
		values = self.timeMap.get(key, [])
		
		# key not in time map
		if not values:
			return ""
		
		left, right = 0, len(values) - 1
		value = ""
		
		while left <= right:
			mid = (left + right) // 2
			num, val = values[mid]
			
			if num <= timestamp:
				value = val
				left = mid + 1
			else:
				right = mid - 1
		
		return value

"""
time complexity:
- O(1) for set
- O(log(n)) for get

space complexity:
- O(m*n); n is the max number of keys, m is the max length of values associated with a key
"""