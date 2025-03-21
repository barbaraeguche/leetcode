# name: 412. fizz buzz
# link: https://leetcode.com/problems/fizz-buzz

# solution #
class Solution:
	def fizzBuzz(self, n: int) -> List[str]:
		fizz = []
		
		for x in range(1, n + 1):
			if x % 15 == 0:
				fizz.append("FizzBuzz")
			elif x % 3 == 0:
				fizz.append("Fizz")
			elif x % 5 == 0:
				fizz.append("Buzz")
			else: fizz.append(str(x))
		
		return fizz
