TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining >= 1:

    print('There are {} tickets remaining'.format(tickets_remaining))

    name = input('What is your name: ')

    num_tickets = input('How many tickets do you want {} '.format(name))
    try:
        num_tickets = int(num_tickets)
    except ValueError:
        print('Oh no we ran into an error')

    amount_tickets = num_tickets * TICKET_PRICE
    print('The total due is ${}'.format(amount_tickets))

    should_proceed = input('You want to buy more tickets\n Enter Y/N ')
    if should_proceed.lower() == 'y':
        print('SOLD')
        tickets_remaining -= num_tickets
    else:
        print('Thank you anyways {}!'.format(name))

print('All tickets are sold out')
