import re

class Calculator(object):
    def __init__(self):
        pass

    def add(self, numbers):
        if numbers == "":
            return 0
        res = 0

        split_numbers=re.split(r',|\n', numbers)

        for i in split_numbers:
            res += self.__parse_int(i)
        return res

    def __parse_int(self, numbers):
        return int(numbers)
