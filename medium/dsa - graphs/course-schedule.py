# name: 207. course schedule
# link: https://leetcode.com/problems/course-schedule

# solution #
class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		incoming, adjacentList = [0] * numCourses, defaultdict(list)
		
		# build an adjacent list
		for src, dest in prerequisites:
			adjacentList[src].append(dest)
			# keep track of in-degree nodes
			incoming[dest] += 1
		
		queue = deque()
		
		# start with vertices that have no in-degree nodes
		for i in range(numCourses):
			if incoming[i] == 0:
				queue.append(i)
		
		schedule = []
		
		while queue:
			node = queue.popleft()
			# add vertex to schedule
			schedule.append(node)
			
			for dest in adjacentList[node]:
				# remove the current incoming node
				incoming[dest] -= 1
				
				# if there are no in-degree nodes, add to queue
				if incoming[dest] == 0:
					queue.append(dest)
			
			# visited this node
			del adjacentList[node]
		
		# if a cycle was found
		if len(schedule) != numCourses:
			return False
		
		return True

"""
time complexity:
- O(v + e); v is the number of vertices, e is the number of edges

space complexity:
- O(v + e)
"""