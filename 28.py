## even = /2
## odd != /2

print('Welcome In The Even-Odd Game')
print('Please Enetr A Number ... And I Will Tell You if it Even Or Odd')
print('If You Wanna Close The Game Enetr X ')

while True:
    number = input('Enter A Number : ')

    if number == 'x':
        print('Closing The Game')
        print('Thanks ...')
        break

    #even number % 2 = 0


    try :
        number = int(number)
        if number % 2 == 0 :
            print('Even Number ')

        else:
            print('Odd Number')
            
    except ValueError:
        print('Please Enetr A Valid Number ')

    print('------------------------------------')
