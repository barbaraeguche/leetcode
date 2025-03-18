# name: 136. single number
# link: https://leetcode.com/problems/single-number

# solution #
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    # get the dict using counter
    counter_nums = Counter(nums)
    # get min value, returns as tuple
    min_value = min(counter_nums.items(), key=lambda x: x[1])

    return min_value[0]
