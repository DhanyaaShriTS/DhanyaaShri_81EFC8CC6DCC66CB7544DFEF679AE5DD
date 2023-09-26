class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
def sort_student(student_list):
  sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
  return sorted_students
students=[Student("Hari","A123",7.8),Student("Srikanth","A124",8.3),Student("Soumya","a125",9.1),Student("Mahesh","A126",9.9)]
sorted_students=sort_student(students)
for student in sorted_students:
  print("Name:{},Roll Number:{}.CGPA:{}".format(student.name,student.roll_number,student.cgpa))