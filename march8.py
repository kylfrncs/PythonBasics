class Student:
    def __init__(self, name, age, yearlevel):
        self.name = name
        self.age = age 
        self.yearlevel = yearlevel 
        
        
    def introduce_self(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Year Level: {self.yearlevel}")
        
    


enrolled_students = []
student1 = Student('Jemima', '19', '3rd year')
enrolled_students.append(student1)

student2 = Student('Karen', '19', '3rd year')
enrolled_students.append(student2)

student3 = Student('Reuben', '19', '3rd year')
enrolled_students.append(student3)

student4 = Student('Kyle', '19', '3rd year')
enrolled_students.append(student4)

student5 = Student('Dionard', '19', '3rd year')
enrolled_students.append(student5)


for i in enrolled_students:
    i.introduce_self()