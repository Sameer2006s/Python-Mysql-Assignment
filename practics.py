class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

a=student("Rajan", 42)
b=student("Rajani", 24)
c=student("Shiwam", 44)
d=student("shiwmi", 29)
e=student("jotis", 43)
a.display()
b.display()
c.display()
d.display()
e.display()

# read student

students = [a, b, c, d, e]
for student in students:
    student.display()

# update student 
# update1=int(input())
new_name = int(input())
new_age = int(input())

students[3].name=new_name
students[3].name=new_name






