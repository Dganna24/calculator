class Calculator:
    def add(self, a, b):
        """Sudėtis: grąžina a + b."""
        return a + b

    def subtract(self, a, b):
        """Atimtis: grąžina a - b."""
        return a - b

    def multiply(self, a, b):
        """Daugyba: grąžina a * b."""
        return a * b

    def divide(self, a, b):
        """Dalyba: grąžina a / b, jei b nėra 0."""
        if b == 0:
            raise ValueError("Dalyba iš nulio negalima.")
        return a / b

    def power(self, a, b):
        """Laipsnio kėlimas: grąžina a ^ b."""
        return a ** b

if __name__ == "__main__":
    calc = Calculator()
    print("2 + 3 =", calc.add(2, 3))
    print("5 - 2 =", calc.subtract(5, 2))
    print("4 * 3 =", calc.multiply(4, 3))
    print("8 / 2 =", calc.divide(8, 2))
    print("2 ^ 3 =", calc.power(2, 3))
