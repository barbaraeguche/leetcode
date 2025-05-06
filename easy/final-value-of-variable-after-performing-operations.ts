// name: 2011. final value of variable after performing operations
// link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations

// solution //
function finalValueAfterOperations(operations: string[]): number {
	let init = 0;
	
	operations.forEach((op) => {
		if (op === "--X") --init;
		else if (op === "X--") init--;
		
		else if (op === "++X") ++init;
		else if (op === "X++") init++;
	});
	
	return init;
};