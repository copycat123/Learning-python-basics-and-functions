import math


def split_check(total, num_of_people):
    cost_per_person = math.ceil(total / num_of_people)
    return cost_per_person


try:
    total_due = float(input('what is the total '))
    num_of_people = int(input('How many people: '))

except ValueError:
    print("that's not the correct value. Try again...")

else:
    amount_due = split_check(total_due, num_of_people)
    print("Each person owes {} rupees".format(amount_due))
