// name: 2667. create hello world function
// link: https://leetcode.com/problems/create-hello-world-function

// solution //
function createHelloWorld() {
	return function(...args): string {
		return "Hello World";
	};
};