class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b


    def add(self):
        return self.a + self.b


    def mul(self):
        return self.a * self.b


class scientific(calculator):

    def power(self):
        return self.a ** self.b






x = scientific(2,3)    
