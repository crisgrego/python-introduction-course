# class Student(object):
#     """Student"""
#     number_of_students = 0

#     def __init__(self, name, index):
#         self.name = name
#         self.index = index
#         Student.number_of_students += 1
#     def __del__(self):
#         Student.number_of_students -= 1

# s1 = Student('Jonh Smith', 33222)
# s2 = Student('Some Guy', 22332)
# print(Student.number_of_students)
# del s1
# print(Student.number_of_students)