"use strict";

class Calculator {
    constructor() {
        this._defaultValue = 0;
    }

    add(numbers) {
        if (this._isEmpty(numbers)) {
            return this._defaultValue;
        }

        if (this._isSingleNumber(numbers)) {
            return this._parseSingleNumber(numbers);
        }

        return this._parseTwoNumbers(numbers);
    }

    _parseTwoNumbers(numbers) {
        return numbers.split(',').reduce((a, b) => {
            return this._parseSingleNumber(a) + this._parseSingleNumber(b)
        });
    }

    _isSingleNumber(numbers) {
        return numbers.indexOf(',') === -1;
    }

    _parseSingleNumber(numbers) {
        return parseInt(numbers, 10);
    }

    _isEmpty(numbers) {
        return !numbers;
    }
}

module.exports = Calculator;