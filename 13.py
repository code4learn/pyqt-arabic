def prinme(arg , *vartuple):
    print('Output')

    #print(arg)
    #print(vartuple)
    #print('--------------')

    result = arg
    for var in vartuple :
        result = result + var

    print(result)
        


#prinme(10 , 20 , 30 , 40 , 50)
