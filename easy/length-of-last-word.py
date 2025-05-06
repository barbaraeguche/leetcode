# name: 58. length of last word
# link: https://leetcode.com/problems/length-of-last-word

# solution #
class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    return len(s.split()[-1])
