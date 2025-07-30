# name: 690. employee importance
# link: https://leetcode.com/problems/employee-importance

# solution #
class Solution:
	def getImportance(self, employees: List['Employee'], id: int) -> int:
		importanceMap = defaultdict(int)
		adjacentList = defaultdict(list)
		
		# build an adjacent list
		for emp in employees:
			importanceMap[emp.id] = emp.importance
			adjacentList[emp.id].extend(emp.subordinates)
		
		queue = deque()
		
		# direct subordinates of employee with give id
		queue.extend(adjacentList[id])
		# importance of employee with give id
		totalImportance = importanceMap[id]
		
		while queue:
			employee = queue.popleft()
			
			# sum its importance
			totalImportance += importanceMap[employee]
			
			# loop through direct employees
			if adjacentList[employee]:
				queue.extend(adjacentList[employee])
		
		return totalImportance
	
"""
time complexity:
- O(n)

space complexity:
- O(n)
"""