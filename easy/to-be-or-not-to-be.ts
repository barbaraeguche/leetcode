// name: 2704. to be or not to be
// link: https://leetcode.com/problems/to-be-or-not-to-be

// solution //
type ToBeOrNotToBe = {
	toBe: (val: any) => boolean;
	notToBe: (val: any) => boolean;
};

function expect(val1: any): ToBeOrNotToBe {
	return {
		toBe(val2: any): boolean {
			const isEqual = val1 === val2;
			
			if (!isEqual) throw new Error("Not Equal");
			return isEqual;
		},
		notToBe(val2: any) {
			const isNotEqual = val1 !== val2;
			
			if (!isNotEqual) throw new Error("Equal");
			return isNotEqual;
		}
	};
};