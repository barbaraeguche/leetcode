# name: 1700. number of students unable to eat lunch
# link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch

# solution #
class Solution:
	def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
		# keep track of the number of students who like each sandwich
		studentCircular, studentSquare = students.count(0), students.count(1)
		
		for sandwich in sandwiches:
			# if there is a circular sandwich but no student
			if sandwich == 0 and studentCircular == 0:
				return studentSquare
			
			# if there is a square sandwich but no student
			if sandwich == 1 and studentSquare == 0:
				return studentCircular
			
			# reduce the count of either student preference
			if sandwich == 0:
				studentCircular -= 1
			else:
				studentSquare -= 1
		
		return 0
