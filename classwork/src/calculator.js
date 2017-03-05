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

        if(this._isSingleNumber(numbers)) {
            return this._parseSingleNumber(numbers);
        }
        return this._parseSingleNumber(numbers[0]) + this._parseSingleNumber(numbers[2]);
    }

    _isSingleNumber(numbers) {
        return numbers.indexOf(",") === -1;
    }

    _parseSingleNumber(numbers) {
        return parseInt(numbers);
    }

    _isEmpty(numbers) {
        return !numbers;
    }
}

module.exports = Calculator;