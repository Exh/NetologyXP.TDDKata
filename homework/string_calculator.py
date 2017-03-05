
class Calculator(object):
    def __init__(self):
        pass

    def add(self, numbers):
        if numbers == "":
            return 0
        res = 0
        split_numbers = numbers.split(",")
        for i in split_numbers:
            res += self.__parseInt(i)
        return res

    def __parseInt(self, numbers):
        return int(numbers)
