import generator

def run():
    """
    Main function
    """
    card_checker_is_ON = True
    while card_checker_is_ON:
        user_input = input(
            'would you like to check if your card is valid? yes/no: ')
        if user_input.lower() == 'yes':
            card = generator.CreditCard()
            if card.has_16_digits and card.is_valid:
                print("your Visa card is valid! Have a nice day :)")
        elif user_input.lower() == 'no':
            card_checker_is_ON = False
            print('Thank you for using the VISTA App! See you soon :)')
        else:
            print("invalid input.")


if __name__ == '__main__':
    run()
