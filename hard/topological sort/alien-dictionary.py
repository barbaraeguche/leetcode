# name: 269. alien dictionary
# link: https://leetcode.com/problems/alien-dictionary

# solution #
class Solution:
	def alienOrder(self, words: List[str]) -> str:
		adjacency = { char: set() for word in words for char in word }
		incoming = { char: 0 for char in adjacency }
		
		for i in range(1, len(words)):
			w1, w2 = words[i-1], words[i]
			minLen = min(len(w1), len(w2))
			
			# x cannot be larger than y and have the same prefix
			if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
				return ""
			
			for j in range(minLen):
				if w1[j] != w2[j]:
					# avoiding duplication
					if w2[j] not in adjacency[w1[j]]:
						adjacency[w1[j]].add(w2[j])
						incoming[w2[j]] += 1
					break
		
		queue = deque([i for i in incoming if not incoming[i]])
		dictionary = []
		
		while queue:
			node = queue.popleft()
			# add vertex to schedule
			dictionary.append(node)
			
			for dest in adjacency[node]:
				# remove the current incoming node
				incoming[dest] -= 1
				
				# if there are no in-degree nodes, add to queue
				if incoming[dest] == 0:
					queue.append(dest)
			
			# visited this node
			del adjacency[node]
		
		if len(dictionary) != len(incoming):
			return ""
		
		return "".join(dictionary)

"""
time complexity:
- O(n * k + v + e); n is the number of words, k is the average length of each word, v is the number of vertices, and e is the number of edges

space complexity:
- O(v + e)
"""