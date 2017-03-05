"use strict";

class Calculator
{
    constructor() {
        this._defaultValue = 0;
    }

    add (numbers) {
        if (this.isEmpty(numbers)) {
            return this._defaultVa
            lue;
        }
        return 1;
    }

    isEmpty(numbers) {
        return !numbers;
    }
}

module.exports = Calculator;