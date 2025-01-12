from random import randint

def get_numbers_ticket(min, max, quantity):
    if min >= max or quantity <= 0 or max - min + 1 < quantity:
        return []
    
    result = set()
    while len(result) < quantity:
        result.add(randint(min, max))
    numbers = sorted(list(result))
    return numbers


lottery_numbers_1 = get_numbers_ticket(1, 100, 6)
lottery_numbers_2 = get_numbers_ticket(-10, 10, 5)
print("Ваші лотерейні числа:", lottery_numbers_1)
print("Ваші лотерейні числа:", lottery_numbers_2)
