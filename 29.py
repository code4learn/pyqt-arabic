print('This Game Will Take Several Numbers And Print The Average Of Them')


count = int(input('how Many Numbers Would You Like To Sum : '))


current_count = 0
summ = 0

while current_count < count :
    number = float(input('Enter The Number : '))
    summ += number
    current_count += 1



print('Summ Of All Numbers = ' , summ)
print('Average Of All Numbers = ' , summ/count)
#print(type(summ))
