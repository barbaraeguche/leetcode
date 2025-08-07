package backtracking

// name: 40. combination sum ii
// link: https://leetcode.com/problems/combination-sum-ii

// solution //
import "slices"

func combinationSum2(candidates []int, target int) [][]int {
	// sort the array
	slices.Sort(candidates)

	n := len(candidates)
	var combinations [][]int

	var validCombSum func(i, target int, path []int)
	validCombSum = func(i, target int, path []int) {
		// found a combination sum
		if target == 0 {
			pathCopy := make([]int, len(path))
			copy(pathCopy, path)

			combinations = append(combinations, pathCopy)
			return
		}

		// invalid combination
		if target < 0 {
			return
		}

		for i < n {
			num := candidates[i]
			// take current num
			path = append(path, num)

			// find all possible combinations
			validCombSum(i+1, target-num, path)
			// backtrack
			path = path[:len(path)-1]

			// avoid duplicates
			for i+1 < n && candidates[i] == candidates[i+1] {
				i += 1
			}

			i += 1
		}
	}

	validCombSum(0, target, []int{})
	return combinations
}

/**
time complexity:
- O(n * 2^n)

space complexity:
- O(n)
*/
