# name: 482. license key formatting
# link: https://leetcode.com/problems/license-key-formatting

# solution #
class Solution:
	def licenseKeyFormatting(self, s: str, k: int) -> str:
		joined = []
		
		no_dash = s.replace("-", "")
		rem = len(no_dash) % k
		
		joined = [no_dash[i:i+k] for i in range(rem, len(no_dash), k)]
		
		if rem != 0:
			joined = [no_dash[:rem]] + joined
		
		return "-".join(joined).upper()