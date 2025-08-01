// name: 2635. apply transform over each element in array
// link: https://leetcode.com/problems/apply-transform-over-each-element-in-array

// solution //
function map(arr: number[], fn: (n: number, i: number) => number): number[] {
	for (let i = 0; i < arr.length; i++) {
		arr[i] = fn(arr[i], i);
	}
	return arr;
}