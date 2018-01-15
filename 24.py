class A:
    def dothis(self):
        print('i am in A')


class B(A):
    pass



class C:
    def dothis(self):
        print('I AM In C')


class D(B , C):
    pass


s = D()
s.dothis()
print(D.mro())
