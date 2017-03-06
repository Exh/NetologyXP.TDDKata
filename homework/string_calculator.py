import re


class Calculator(object):
    def __init__(self, p=None):
        self.separators = ',|\n'
        if p:
            self.separators += '|' + p

    def add(self, numbers):
        if numbers == "":
            return 0
        res = 0

        split_numbers = re.split(self.separators, numbers)

        for i in split_numbers:
            res += self.__parse_int(i)
        return res

    @classmethod
    def __parse_int(cls, numbers):
        return int(numbers)
