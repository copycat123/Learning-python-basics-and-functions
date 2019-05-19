TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100


def calculate_price(num_tickets):
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1:

    print('There are {} tickets remaining'.format(tickets_remaining))

    name = input('What is your name: ')

    num_tickets = input('How many tickets do you want {} '.format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError(
                'There are only {} tickets remaining'.format(tickets_remaining))
    except ValueError as error:
        print('Oh no we ran into an error.{}'.format(error))
    else:
        num_tickets = int(num_tickets)

        amount_tickets = calculate_price(num_tickets)
        print('The total due is ${}'.format(amount_tickets))

        should_proceed = input('You want to buy more tickets\n Enter Y/N ')
        if should_proceed.lower() == 'y':
            print('SOLD')
            tickets_remaining -= num_tickets
        else:
            print('Thank you anyways {}!'.format(name))

print('All tickets are sold out')
