class student:
    def __init__(self , name):
        self.name = name
        self.marks = []
        print('welcome {} in the school' .format(name))



    def add_marks(self , mark):
        self.marks.append(mark)


    def avg(self):
        return sum(self.marks)/len(self.marks)



s1 = student('mahmoud')

print(s1.marks)

s1.add_marks(40)
s1.add_marks(50)
s1.add_marks(30)
s1.add_marks(80)
s1.add_marks(60)

print(s1.marks)


print(s1.avg())
