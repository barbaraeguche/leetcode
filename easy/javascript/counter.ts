// name: 2620. counter
// link: https://leetcode.com/problems/counter

// solution //
function createCounter(n: number): () => number {
	return function() {
		return n++;
	};
}

/**
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */