# name: 929. unique email addresses
# link: https://leetcode.com/problems/unique-email-addresses

# solution #
class Solution:
	def numUniqueEmails(self, emails: List[str]) -> int:
		seen = set()
		
		for email in emails:
			local, domain = email.split("@")
			
			string = ""
			
			# normalize the local name
			for char in local:
				if char == "+":
					break
				if char == ".":
					continue
				
				string += char
			
			# add normalized email to set
			seen.add(f"{string}@{domain}")
		
		return len(seen)
	
"""
time complexity:
- O(n * l); l is the length of the local name

space complexity:
- O(n)
"""