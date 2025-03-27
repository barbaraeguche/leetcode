# name: 2469. convert the temperature
# link: https://leetcode.com/problems/convert-the-temperature

# solution #
class Solution:
	def convertTemperature(self, celsius: float) -> List[float]:
		return [celsius + 273.15, celsius * 1.80 + 32.00]