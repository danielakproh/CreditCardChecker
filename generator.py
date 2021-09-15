import random
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class CreditCard:
    def __init__(self) -> None:
        self.card_number = input("please enter your card number to check: ")
        self.card_digits = [char for char in self.card_number]

    def has_16_digits(self) -> bool:
        """ 
        Check if card has 16 digits

        parameters:
                    None

        returns: 
                    Boolean: True if card has 16 digits
        """

        if len(self.card_number) == 16:
            return True
        else:
            while len(self.card_number) != 16:
                if len(self.card_number) > 16 or len(self.card_number) < 16:
                    print("Invalid input. Please enter 16 digits.")
                    self.card_number = input(
                        "please enter your card number to check: ")
        return True

    def is_valid(self):
        """
        Check card's validity using the Luhn's algorithm

        parameters:
                    None

        returns: 
                    Boolean: True if card number satisphies the Luhn's algorithm
                    Boolean: False if card number does not satisphies the Luhn's algorithm
        """
        
        # doubling each digit starting from second to last
        for i in range(1, 16, 2):
            self.card_digits[-i-1] = str(2 * int(self.card_digits[-i-1]))
        print(f"after doubling each two digit we get {self.card_digits}")

        # adding up elements made up of 2 digits
        summed_digits = []
        for element in self.card_digits:
            if len(element) == 2:
                summed_digits.append(int(element[0]) + int(element[1]))
            else:
                summed_digits.append(element)
        print(f"after adding 2-digit numbers we get {summed_digits}")

        # adding up all digits
        total_sum = 0
        for digit in summed_digits:
            total_sum += int(digit)
        print(f"the total sum is {total_sum}")

        # checking divisibility by 10
        if total_sum % 10 == 0:
            return True
        else:
            return False


def generate(self):
    """generate card number that satisfies the Luhn's algorithm"""
    pass
