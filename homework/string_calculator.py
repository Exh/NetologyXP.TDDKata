
class Calculator(object):
    def __init__(self):
        pass

    def add(self, numbers):
        if ',' in numbers:
            return self.__parseInt(numbers[0]) + self.__parseInt(numbers[2])
        elif numbers == "":
            return 0
        return self.__parseInt(numbers)

    def __parseInt(self, numbers):
        return int(numbers)
