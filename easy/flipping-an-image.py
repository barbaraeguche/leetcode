# name: 832. flipping an image
# link: https://leetcode.com/problems/flipping-an-image

# solution #
class Solution:
	def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
		for i, img in enumerate(image):
			flip = img[::-1]
			invert = [1 if x == 0 else 0 for x in flip]
			
			image[i] = invert
		
		return image
