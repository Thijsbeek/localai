import sys
sys.path.insert(0, 'pkg')
from calculator import Calculator

def test_calculator():
    calc = Calculator()
    result = calc.evaluate("3 + 7 * 2")
    print(f"3 + 7 * 2 = {result}")
    assert result == 17, f"Expected 17, got {result}"
    print("Test passed!")

if __name__ == "__main__":
    test_calculator()