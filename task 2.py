from random import randint

def get_numbers_ticket(min, max, quantity):
    result = set()
    while len(result) < quantity:
        result.add(randint(min, max))
    numbers = sorted(list(result))
    return numbers


lottery_numbers = get_numbers_ticket(1, 100, 6)
print("Ваші лотерейні числа:", lottery_numbers)
