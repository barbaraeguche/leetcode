# name: 210. course schedule iv
# link: https://leetcode.com/problems/course-schedule-iv

# solution #
class Solution:
	def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
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
		
		preReqSet = [set() for _ in range(numCourses)]
		
		while queue:
			node = queue.popleft()
			
			for dest in adjacentList[node]:
				# add the parent as a prereq
				preReqSet[dest].add(node)
				# add all prereq of parent
				preReqSet[dest].update(preReqSet[node])
				
				# remove the current incoming node
				incoming[dest] -= 1
				
				# if there are no in-degree nodes, add to queue
				if incoming[dest] == 0:
					queue.append(dest)
			
			# visited this node
			del adjacentList[node]
		
		return [src in preReqSet[dest] for src, dest in queries]

"""
time complexity:
- O(v(v + e) + m); v is the number of courses, e is the number of prerequisites, m is the number of queries

space complexity:
- O(v^2 + e + m)
"""