class Calc:
    sum = lambda x, y: x + y
    mult = lambda x, y: x * y
    
print(Calc.sum(Calc.mult(2, 7), Calc.mult(3, 5)))