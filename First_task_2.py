import random

def get_numbers_ticket(min, max, quantity):
    #validating parameters data
    if (str(min) + str(max) +str(quantity)).isdigit() and max > min and min > 0 and max <= 1000 and quantity <= (max - min):
        #generate full set
        set_numbers_ticket = set()
        #generate set of numbers
        while len(set_numbers_ticket) < quantity:
            number = random.randrange(min, max)
            set_numbers_ticket.add(number)
        #get list from set
        set_numbers_ticket = list(set_numbers_ticket)
        return set_numbers_ticket
    else:
        return []

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)