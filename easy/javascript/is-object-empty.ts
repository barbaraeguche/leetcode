// name: 2727. is object empty
// link: https://leetcode.com/problems/is-object-empty

// solution //
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | JSONValue[]

function isEmpty(obj: Obj): boolean {
	return Object.keys(obj).length === 0;
};