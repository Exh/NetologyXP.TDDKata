
class Calculator(object):
    def __init__(self):
        pass

    def add(self, numbers):
        if ',' in numbers:
            split_numbers = numbers.split(",")
            return self.__parseInt(split_numbers[0]) + self.__parseInt(split_numbers[1])
        elif numbers == "":
            return 0
        return self.__parseInt(numbers)

    def __parseInt(self, numbers):
        return int(numbers)
