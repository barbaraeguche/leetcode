# name: 1. two sum
# link: https://leetcode.com/problems/two-sum

# solution #
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    idx_dict = {}
        
    for i, x in enumerate(nums):
      complement = target - x
      if complement in idx_dict:
        return [idx_dict[complement], i]

      idx_dict |= { x: i }
    return []
