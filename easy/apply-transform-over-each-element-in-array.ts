// name: 2635. apply transform over each element in array
// link: https://leetcode.com/problems/apply-transform-over-each-element-in-array

// solution //
function map(arr: number[], fn: (n: number, i: number) => number): number[] {
	let new_arr = [...arr];
	
	for (let i = 0; i < arr.length; i++) {
		new_arr[i] = fn(arr[i], i);
	}
	
	return new_arr;
};