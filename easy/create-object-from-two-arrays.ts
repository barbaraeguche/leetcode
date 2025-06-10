// name: 2794. create object from two arrays
// link: https://leetcode.com/problems/create-object-from-two-arrays

// solution //
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function createObject(keysArr: JSONValue[], valuesArr: JSONValue[]): Record<string, JSONValue> {
	let object = {}
	
	for (let i = 0; i < keysArr.length; i++) {
		const key = `${keysArr[i]}`, val = valuesArr[i];
		
		if (!object.hasOwnProperty(key)) {
			object[key] = val;
		}
	}
	
	return object;
};