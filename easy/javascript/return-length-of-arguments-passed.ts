// name: 2703. return length of arguments passed
// link: https://leetcode.com/problems/return-length-of-arguments-passed

// solution //
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function argumentsLength(...args: JSONValue[]): number {
	return [...args].length;
};