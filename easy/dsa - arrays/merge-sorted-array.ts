// name: 88. merge sorted array
// link: https://leetcode.com/problems/merge-sorted-array

// solution //
/**
Do not return anything, modify nums1 in-place instead.
*/
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
	const slices = [...nums1.slice(0, m), ...nums2].sort((a, b) => a - b);

	for (let i = 0; i < slices.length; i++) {
		nums1[i] = slices[i]
	}
};