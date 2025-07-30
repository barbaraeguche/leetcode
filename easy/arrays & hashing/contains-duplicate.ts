// name: 217. contains duplicate
// link: https://leetcode.com/problems/contains-duplicate

// solution //
function containsDuplicate(nums: number[]): boolean {
	return nums.length != (new Set(nums)).size;
}