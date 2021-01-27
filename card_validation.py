import re
from datetime import date, datetime

'''Validating credit card number using Luhn's algorithm'''
def validate_card(card_number):
    card_number = list(card_number)
    check_digit = card_number.pop()
    card_number.reverse()
    sol = []

    for index, num in enumerate(card_number):
        if index % 2 == 0:
            num = int(num) * 2
            if num > 9:
                num -= 9
            sol.append(num)
        else:
            sol.append(int(num))

    total = int(check_digit) + sum(sol)
    if total % 10 == 0:
        return True
    return False


'''Validating name using regex'''
def validate_name(name):
    if bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name)):
        return True
    return False


'''Validating date to prevent past expiration date'''
def validate_date(exp_date):
    exp_date = datetime.strptime(exp_date, '%d-%m-%Y').date()
    if date.today() > exp_date:
        return True
    return False


'''Validating amount to be positive number'''
def validate_amount(amount):
    if amount > 0:
        return True
    return False
