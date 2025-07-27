// name: 2666. allow one function call
// link: https://leetcode.com/problems/allow-one-function-call

// solution //
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type OnceFn = (...args: JSONValue[]) => JSONValue | undefined

function once(fn: Function): OnceFn {
	let hasBeenCalled = false;
	
	return function (...args) {
		if (!hasBeenCalled) {
			hasBeenCalled = true;
			return fn(...args);
		}
	};
}

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */