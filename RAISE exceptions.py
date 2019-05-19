import math


def split_check(total, num_of_people):
    if num_of_people <= 1:        # Make condition if there is not a single person to split the check
        raise ValueError('More than 1 person is required to split the check')
    cost_per_person = math.ceil(total / num_of_people)
    return cost_per_person


try:
    total_due = float(input('what is the total '))
    num_of_people = int(input('How many people: '))
    amount_due = split_check(total_due, num_of_people)

except ValueError as error:    # create the new variable called error
    print("that's not the correct value. Try again...")
    # If there is not a single person to split a check
    print('There is no such thing as 0 people')
else:

    print("Each person owes {} rupees".format(amount_due))
