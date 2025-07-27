// name: 2665. counter ii
// link: https://leetcode.com/problems/counter-ii

// solution //
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
	let num = init;
	return {
		increment: () => ++num,
		decrement: () => --num,
		reset: () => num = init
	};
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */