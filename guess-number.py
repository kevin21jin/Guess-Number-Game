# try to guess the random number range from 1 to 100, you have 5 tries in total

import random

target = random.randint(1, 100)

i = 1
while i <= 5:
    n = int(input('input: '))
    if n > target:
        print('too large')
    elif n < target:
        print('too small')
    else:
        print('correct')
        break
    i += 1
if i > 5:
    print(f'failed, the answer is {target}')
