# name: 811. subdomain visit count
# link: https://leetcode.com/problems/subdomain-visit-count

# solution #
class Solution:
	def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
		domainMap = defaultdict(int)
		
		for domain in cpdomains:
			count, dom = domain.split()
			doms = dom.split(".")
			
			for i in range(len(doms)):
				subdomain = ".".join(doms[-i-1:])
				domainMap[subdomain] += int(count)
		
		return [f"{val} {key}" for key, val in domainMap.items()]

"""
time complexity:
- O(n * m)

space complexity:
- O(n * m)
"""