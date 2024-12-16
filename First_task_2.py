import random

def get_numbers_ticket(min, max, quantity):
    #validating parameters data
    if (str(min) + str(max) +str(quantity)).isdigit() and max > min and min > 1 and max <= 1000 and quantity <= (max - min):
        #generate full set
        set_numbers_ticket = set()
        #generate set of numbers
        while len(set_numbers_ticket) < quantity:
            number = random.randrange(min, max)
            set_numbers_ticket.add(number)
        return set_numbers_ticket
    else:
        return []

print(get_numbers_ticket(2, 12, 6))