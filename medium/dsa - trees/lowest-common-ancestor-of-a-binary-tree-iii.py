# name: 1650. lowest common ancestor of a binary tree iii
# link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii

# solution #
class Solution:
	def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
		seen = set()
		
		# traverse together
		while p and q:
			# store visited nodes
			seen.add(p.val)
			seen.add(q.val)
			
			p = p.parent
			q = q.parent
			
			# they share a unique parent
			if p and q and p.val == q.val:
				return p
			
			# if one is a parent of the other
			if p and p.val in seen:
				return p
			if q and q.val in seen:
				return q
		
		# p is a child of q
		while p:
			seen.add(p.val)
			p = p.parent
			
			if p and p.val in seen:
				return p
		
		# q is a child of p
		while q:
			seen.add(q.val)
			q = q.parent
			
			if q and q.val in seen:
				return q
		
		return None
	
"""
time complexity:
- O(h)

space complexity:
- O(n); n is the number of node values
"""