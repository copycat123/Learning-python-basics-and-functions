name = input("What's your name? ")
understand = input(
    '{} do you understand python while loops?\n Enter yes/no: '.format(name))

while understand.lower() != 'yes':
    print('ok {}, while loops in Pyton repeat as long as a certain Boolean condition is met.'.format(name))
    print('{}, now do you understand python while loops'.format(name))
    understand = input(
        '{} do you understand python while loops?\n Enter yes/no: '.format(name))
print('i am very happy that you understand while loops now'.format(name))
