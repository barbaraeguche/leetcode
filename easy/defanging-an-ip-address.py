# name: 1108. defanging an ip address
# link: https://leetcode.com/problems/defanging-an-ip-address

# solution #
class Solution:
	def defangIPaddr(self, address: str) -> str:
		return address.replace('.', '[.]')