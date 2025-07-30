# name: 721. accounts merge
# link: https://leetcode.com/problems/accounts-merge

# solution #
class UnionFind:
	def __init__(self, n):
		self.parent = {}
		self.rank = {}
		
		for i in range(n):
			self.parent[i] = i
			self.rank[i] = 0
	
	def find(self, n):
		if n != self.parent[n]:
			self.parent[n] = self.find(self.parent[n])
		return self.parent[n]
	
	def union(self, n1, n2):
		p1, p2 = self.find(n1), self.find(n2)
		
		# already share a parent
		if p1 == p2:
			return False
		
		if self.rank[p1] < self.rank[p2]:
			self.parent[p1] = p2
		elif self.rank[p2] < self.rank[p1]:
			self.parent[p2] = p1
		else:
			self.parent[p1] = p2
			self.rank[p2] += 1
		
		return True

class Solution:
	def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
		uf = UnionFind(len(accounts))
		emailIdxMap = {}  # map each email to the index of account
		
		# create a disjoint set
		for idx, acct in enumerate(accounts):
			for email in acct[1:]:
				if email in emailIdxMap:
					uf.union(idx, emailIdxMap[email])
				else:
					emailIdxMap[email] = idx
		
		emailGroup = defaultdict(list)
		
		# group the emails by their root parent
		for email, idx in emailIdxMap.items():
			emailGroup[uf.find(idx)].append(email)
		
		mergedAccounts = []
		
		# merge the accounts
		for idx, emails in emailGroup.items():
			owner, emails = accounts[idx][0], sorted(emails)
			mergedAccounts.append([owner] + emails)
		
		return mergedAccounts

"""
time complexity:
- O(n * m * log(n * m)); n is the number of accounts, m is the number of emails

space complexity:
- O(n * m)
"""