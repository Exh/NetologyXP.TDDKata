"use strict"

var assert = require("chai").assert;

var Calculator = require("../src/calculator");


suite("string calculator should", function() {
    function createCalculator() {
        return new Calculator();
    }

    test("return default value if input is empty", function(){
        var calculator = createCalculator();

        var sum = calculator.add(null);

        assert.equal(sum, 0)
    });

    test("return single number if input is single number", function () {
        var calculator = createCalculator();

        var sum = calculator.add("2");

        assert.equal(sum, 2);
    });
    
    test("return sum of two comma separated one-digit numbers", function () {
        var calculator = createCalculator();

        var sum = calculator.add("1,2");

        assert.equal(sum, 1 + 2);
    });

    test("return sum of any two comma separate numbers", function () {
        var calculator = createCalculator();

        var sum = calculator.add("11,22");

        assert.equal(sum, 11 + 22);
    });

    test("return sum of any amount comma separate values", function () {
        var calculator = createCalculator();

        var sum = calculator.add("1,2,3,4,5");

        assert.equal(sum, 1+2+3+4+5);
    });

    test("return sum of two newline separated numbers", function () {
        var calculator = createCalculator();
        var sum = calculator.add("1\n2");
        assert.equal(sum, 1 + 2);
    });
});