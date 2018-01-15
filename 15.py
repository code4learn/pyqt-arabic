f = 0
print(f)   ## f = 0

def testt():
    global f
    f = 5     ### Local f
    print(f)   ## f = 5 


testt()
print(f)    ### ???????




## Local  Vs Global 
