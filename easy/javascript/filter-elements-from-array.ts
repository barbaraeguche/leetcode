// name: 2634. filter elements from array
// link: https://leetcode.com/problems/filter-elements-from-array

// solution //
type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
	let newArr: number[] = [];
	
	for (let i = 0; i < arr.length; i++) {
		if (fn(arr[i], i)) {
			newArr.push(arr[i]);
		}
	}
	return newArr;
}