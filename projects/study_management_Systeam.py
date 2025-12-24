#学生管理系统

class student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.course_list = []
    def add_course(self, course):
        if course not in self.course_list:
            self.course_list.append(course)
            print(f"{self.name} 选择了 {course.course_name}")
            course.add_student(self)
        else:
            print(f"{self.name} 已经选择了 {course.course_name}")
    def remove_course(self, course):
        if course in self.course_list:
            self.course_list.remove(course)
            print(f"{self.name} 取消了 {course.course_name}")
            course.remove_student(self)
        else:
            print(f"{self.name} 没有选择 {course.course_name}")
    def get_course_list(self):
        print(f"{self.name} 选择的课程有：")
        for course in self.course_list:
            print(course.course_name)

class course:
    def __init__(self, course_name, course_amount):
        self.course_name = course_name
        self.course_amount = course_amount
        self.student_list = []
    def add_student(self, student):
        if student not in self.student_list and len(self.student_list) < self.course_amount:
            self.student_list.append(student)
            print(f"{self.course_name} 增加了 {student.name}")
            self.course_amount + 1
        elif len(self.student_list) >= self.course_amount:
            print(f"{self.course_name} 已经满员了")
        else:
            print(f"{self.course_name} 已经增加了 {student.name}")
    def remove_student(self, student):
        if student in self.student_list:
            self.student_list.remove(student)
            print(f"{self.course_name} 取消了 {student.name}")
        else:
            print(f"{self.course_name} 没有增加 {student.name}")
    def get_student_list(self):
        print(f"{self.course_name} 的学生有：")
        for student in self.student_list:
            print(student.name)
        
zs=student("张三", 18, 1001)
math=course("数学", 30)
zs.add_course(math)
zs.get_course_list()
math.get_student_list()

