import random, time

def waiting_game():
    rand = random.randint(1, 10)

    print('Your target time is {} seconds'.format(rand))
    print('---Press Enter to Begin---')
    
    input()
    print('...Press Enter again after {} seconds...'.format(rand))
    before = time.time()

    input()

    elapsed = time.time()

    calculated = round(elapsed - before, 3)
    print('Elapsed time: {} seconds'.format(calculated))

    if rand > calculated:
        print('{} seconds too fast'.format(round(rand - calculated, 3)))
    elif rand < calculated:
        print('{} seconds too slow'.format(round(calculated - rand, 3)))
    else:
        print('Perfect!')


if __name__ == '__main__':
    waiting_game()
