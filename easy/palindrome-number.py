# name: 9. palindrome number
# link: https://leetcode.com/problems/palindrome-number

# solution #
class Solution:
  def isPalindrome(self, x: int) -> bool:
    int_str = str(x)
    a, b = 0, len(int_str) - 1

    while a < b:
      if int_str[a] != int_str[b]:
        return False
      else:
        a += 1
        b -= 1
            
    return True
