"use strict"

var assert = require("chai").assert;

var Calculator = require("../src/calculator");


suite("string calculator should", function() {
    test("return 0 if input is empty", function(){
        var calculator = new Calculator();

        var sum = calculator.add(null);

        assert.equal(sum, 0)
    });
});