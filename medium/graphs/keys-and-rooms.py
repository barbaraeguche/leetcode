# name: 841. keys and rooms
# link: https://leetcode.com/problems/keys-and-rooms

# solution #
class Solution:
	def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
		kys = rooms[0]
		queue, keys = deque(kys), {0, *kys}
		
		while queue:
			key = queue.popleft()
			
			for ky in rooms[key]:
				if ky not in keys:
					keys.add(ky)
					queue.append(ky)
		
		return len(keys) == len(rooms)
	
"""
time complexity:
- O(v + e); v is the number of rooms, e is the number of edges

space complexity:
- O(n)
"""