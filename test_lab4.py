import pytest

class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self, a, b):
        return a + b
        
    def subtract(self, a, b):
        return a - b
        
    def multiply(self, a, b):
        return a * b
        

calc = Calculator("Calc 1")
@pytest.fixture
def base_calculator():
    return Calculator("Base Calculator")
    
def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)
    
    assert True
    
def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)
    
    assert True

def test_add():
    assert calc.add(1,1) == 2
    assert calc.add(1.0,2.5) == 3.5
    assert calc.add(0,0) == 0
    assert calc.add(-5,-6) == -11
    
def test_subtract():
    assert calc.subtract(1,1) == 0
    assert calc.subtract(-1,1) == -2
    assert calc.subtract(-3.0,-2.5) == -0.5
    assert calc.subtract(5,-1) == 6
    
def test_multiply():
    assert calc.multiply(4,6) == 24
    assert calc.multiply(2.5,2) == 5
    assert calc.multiply(-4,5) == -20
    assert calc.multiply(-6,-3) == 18