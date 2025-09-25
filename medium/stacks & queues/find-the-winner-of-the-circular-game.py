# name: 1823. find the winner of the circular game
# link: https://leetcode.com/problems/find-the-winner-of-the-circular-game

# solution #
class Solution:
	def findTheWinner(self, n: int, k: int) -> int:
		queue = deque([i for i in range(1, n + 1)])
		
		while len(queue) > 1:
			n = len(queue)
			
			# add back to the list
			for _ in range(k - 1):
				queue.append(queue.popleft())
			
			# pop the current loser
			queue.popleft()
		
		return queue.popleft()

"""
time complexity:
- O(n * k);

space complexity:
- O(n)
"""