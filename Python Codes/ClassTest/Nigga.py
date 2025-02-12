class PIG():
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    def calc(self, sign):
        c = self.calculate(self.num1, self.num2, sign)
        return c
    def calculate(self, n1, n2, s):
        if s == "+":
            return n1 + n2
        if s == "-":
            return n1 - n2
        if s == "*":
            return n1 * n2
        if s == "/":
            return n1 / n2
