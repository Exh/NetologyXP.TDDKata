import re


class Calculator(object):
    def __init__(self, p=None):
        self.separators = ',|\n'
        if p:
            self.separators += '|' + p

    def add(self, numbers):
        res = 0

        if len(numbers) > 4 and numbers[3] == '\n' and numbers[0] == '/' and numbers[1] == '/':
            self.separators += '|' + numbers[2]
            numbers = numbers[3:]

        split_numbers = re.split(self.separators, numbers)

        for i in split_numbers:
            res += self.__parse_int(i)
        return res

    @classmethod
    def __parse_int(cls, numbers):
        if numbers == "":
            return 0
        return int(numbers)
