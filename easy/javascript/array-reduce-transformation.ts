// name: 2626. array reduce transformation
// link: https://leetcode.com/problems/array-reduce-transformation

// solution //
type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
	let summation = init;
	
	for (const num of nums) {
		summation = fn(summation, num);
	}
	return summation;
}