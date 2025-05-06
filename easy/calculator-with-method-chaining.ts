// name: 2726. calculator with method chaining
// link: https://leetcode.com/problems/calculator-with-method-chaining

// solution //
class Calculator {
	value: number = 0;
	
	constructor(value: number) {
		this.value = value;
	}
	
	add(value: number): Calculator {
		this.value += value;
		return this;
	}
	
	subtract(value: number): Calculator {
		this.value -= value;
		return this;
	}
	
	multiply(value: number): Calculator {
		this.value *= value;
		return this;
	}
	
	divide(value: number): Calculator {
		if (value === 0) throw new Error("Division by zero is not allowed");
		
		this.value /= value;
		return this;
	}
	
	power(value: number): Calculator {
		this.value = Math.pow(this.value, value);
		return this;
	}
	
	getResult(): number {
		return this.value;
	}
}