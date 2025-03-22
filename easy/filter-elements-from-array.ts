// name: 2634. filter elements from array
// link: https://leetcode.com/problems/filter-elements-from-array

// solution //
type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
	let new_arr: number[] = [];
	
	for (let i = 0; i < arr.length; i++) {
		const notFilter = fn(arr[i], i);
		if (notFilter) new_arr.push(arr[i]);
	}
	
	return new_arr;
};