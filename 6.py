'''
x = 0
while x < 10 :
    print(x)
    x += 1
else:
    print('x >= 10')
print('mahmoud ahmed')
x = 0
while x < 10 : print(x) ; x += 1
'''


x = 0
while x < 5 :        # 0 1 2 3 4
    y = 0            # x = 0   first iteration
    print(x+1 , 'interation')
    while y < 3 :    #y = 0 1 2
        print('x = ' , x , 'y = ', y) # y = 0 first iteration  , x = 0
        #print(y+1 , 'iteration')
        y += 1       # y = 1
                        # 1 , 0 --- 1 , 1 ---- 1 , 2

    x +=1           # x = 1 
