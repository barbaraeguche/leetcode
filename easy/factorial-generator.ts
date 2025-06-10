// name: 2803. factorial generator
// link: https://leetcode.com/problems/factorial-generator

// solution //
function* factorial(n: number): Generator<number> {
	if (n === 0) {
		return 1;
	}
	
	let factorial = 1;
	
	for (let i = 1; i <= n; i++) {
		factorial *= i;
		yield factorial;
	}
};