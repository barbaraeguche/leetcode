# name: 136. single number
# link: https://leetcode.com/problems/single-number

# solution #
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    single = 0
    
    for num in nums:
      single ^= num
      
    return single

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""