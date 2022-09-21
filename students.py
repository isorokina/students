class Student:
    
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def print(self, name, marks):
        print(self.name, self.marks)

student1=Student('Tom', 45)
#student1.print
#print(student1.name, student1.marks)


'''class Student:
    
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

student1=Student('Tom', 45)
print(student1.name, student1.marks)
'''
