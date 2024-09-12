num = int(input('Enter a number: '))

def check_num(num):
    if num % 2 == 0:
        print(f'{num} is an even number')
    else:
        print(f'{num} is an odd number')

check_num(num)

