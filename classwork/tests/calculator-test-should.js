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

    test("return 1 if input 1", function() {
        var calculator = createCalculator();

        var sum = calculator.add("1");

        assert.equal(sum, 1);
    });

    test("return single number if input is single number", function () {
        var calculator = createCalculator();

        var sum = calculator.add("2");

        assert.equal(sum, 2);
    });
});