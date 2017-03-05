"use strict";

class Calculator
{
    constructor() {
        this._defaultValue = 0;
    }

    add (numbers) {
        if (this._isEmpty(numbers)) {
            return this._defaultValue;
        }
        return this._parseSingleNumber(numbers);
    }

    _parseSingleNumber(numbers) {
        return parseInt(numbers);
    }

    _isEmpty(numbers) {
        return !numbers;
    }
}

module.exports = Calculator;