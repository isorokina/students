class Student:
    
    def check_pass_fail(self):
        if self.marks>=40:
            return True
        else:
            return True

    '''def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def izdruka(self, name, marks):
        print(self.name, self.marks)'''

   
student1=Student()
student1.name='Tom'
student1.marks=50
did_pass=student1.check_pass_fail
print(did_pass)
#print(student1.name, student1.marks)


'''class Student:
    
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

student1=Student('Tom', 45)
print(student1.name, student1.marks)
'''
