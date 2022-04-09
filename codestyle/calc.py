"""The module calc allows you to perform simple math operations."""


class Calculator:
    """The Calculator class contains methods for math operations.

    The class has 4 methods:
        1) addition -  get the sum of the given numbers,
        2) subtraction - get the difference between the given numbers,
        3) multiplication - get the product of given numbers,
        4) division - get the quotient of given numbers.
    """

    def __init__(self, *numbers):
        """The method has only one additional argument - *numbers.
        *numbers is a tuple arguments that have to be a numbers."""
        self.numbers = numbers

    def addition(self):
        """The method takes a tuple of numbers and adds numbers one by one.
        The first position in the tuple is assigned to the "add_result" variable
        and the rest are used in for loop to add them to "add_result".
        """
        add_result = self.numbers[0]
        for numb in self.numbers[1:]:
            add_result += numb
        return add_result

    def subtraction(self):
        """The method takes a tuple of numbers and subtracts numbers one by one.
        The first position in the tuple is assigned to the "subt_result" variable and
        the rest are used in for loop to get the difference between "subt_result"
        and the number in the current iteration.
        """
        subt_result = self.numbers[0]
        for numb in self.numbers[1:]:
            subt_result -= numb
        return subt_result

    def multiplication(self):
        """The method takes a tuple of numbers and multiplicates numbers one by one.
        The first position in the tuple is assigned to the "mult_result" variable and
        the rest are used in for loop to get the product of "mult_result"
        and the number in the current iteration.
        """
        mult_result = self.numbers[0]
        for numb in self.numbers[1:]:
            mult_result *= numb
        return mult_result

    def division(self):
        """The method takes a tuple of numbers and divides numbers one by one.
        The first position in the tuple is assigned to the "div_result" variable and
        the rest are used in for loop to get the quotient of "div_result"
        and the number in the current iteration.
        """
        div_result = self.numbers[0]
        for numb in self.numbers[1:]:
            div_result /= numb
        return div_result
