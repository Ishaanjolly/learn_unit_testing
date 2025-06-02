class Student: 
    def __init__(self, name, age, grade):  
        self.name = name 
        self.age = age 
        self.grade = grade 
        self.courses = {}
        
    def add_course(self, course_wise_marks):
        self.courses.update(course_wise_marks)
    
    def get_courses(self):
        return self.courses.copy()

# if __name__ == '__main__':
    
#     register = Student('Aman', 15, 10)
#     register.add_course({'math':50})
#     register.add_course({'science': 78})
#     print(f"student: {register.name}, grade: {register.grade}, age: {register.age}, courses = {register.get_courses()}")
