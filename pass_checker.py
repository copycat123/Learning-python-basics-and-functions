import sys

MASTER_PASSWORD = 'defcon'
attemps_count = 1
password = input('Enter the secret password: ')

while password != MASTER_PASSWORD:
    if attemps_count > 3:
        sys.exit('Too many attemps. Try again later...')
    password = input('Wrong password Try again')
    attemps_count += 1
print('Welcome defcon')
