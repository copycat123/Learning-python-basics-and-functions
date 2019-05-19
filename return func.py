import math


def split_check(total, num_of_people):  # total and num of people are parameters
    # cost per person = total / num_of_people
    cost_per_person = math.ceil(total / num_of_people)
    return cost_per_person  # return the call

    # return math.ceil(total / num_of_people) can be shorten to # cost_per_person = math.ceil(total / num_of_people)
    # return cost_per_person


# change values to arguments total_due and num _of_people
amount_due = split_check(83.27, 4)
total_due = float(input('what is the total '))  # total_due or total
num_of_people = int(input('How many people: '))


print("Each person owes {} rupees".format(amount_due))
