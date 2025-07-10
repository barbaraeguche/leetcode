# name: 210. course schedule ii
# link: https://leetcode.com/problems/course-schedule-ii

# solution #
class Solution:
	def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
		outgoing, adjacentList = [0] * numCourses, defaultdict(list)
		
		# build an adjacent list
		for src, dest in prerequisites:
			adjacentList[dest].append(src)
			# keep track of out-degree nodes
			outgoing[src] += 1
		
		queue = deque()
		
		# start with vertices that have no out-degree nodes
		for i in range(numCourses):
			if outgoing[i] == 0:
				queue.append(i)
		
		schedule = []
		
		while queue:
			node = queue.popleft()
			# add vertex to schedule
			schedule.append(node)
			
			for src in adjacentList[node]:
				# remove the current outgoing node
				outgoing[src] -= 1
				
				# if there are no out-degree nodes, add to queue
				if outgoing[src] == 0:
					queue.append(src)
			
			# visited this node
			del adjacentList[node]
		
		# if a cycle was found
		if len(schedule) != numCourses:
			return []
		
		return schedule

"""
time complexity:
- O(v + e); v is the number of vertices, e is the number of edges

space complexity:
- O(v + e)
"""