# A部分：基础语法和数据类型 - 复习练习题
# 涵盖A.1到A.6所有主题的综合练习

print("=== A部分复习练习题 ===")
print("请完成以下练习来测试你的理解程度")
print()

# 练习1：数据类型和变量（A.1）
print("练习1：数据类型和变量")
print("-" * 30)

# 1.1 创建以下变量并打印它们的类型：
# - 姓名（字符串）
# - 年龄（整数）
# - 身高（浮点数）
# - 是否学生（布尔值）

# 你的代码：
name = "张三"
age = 25
height = 175.5
is_student = True

print(f"姓名: {name}, 类型: {type(name)}")
print(f"年龄: {age}, 类型: {type(age)}")
print(f"身高: {height}, 类型: {type(height)}")
print(f"是否学生: {is_student}, 类型: {type(is_student)}")

print()

# 练习2：数据结构操作（A.2）
print("练习2：数据结构操作")
print("-" * 30)

# 2.1 创建一个学生信息字典
student_info = {
    "姓名": "李四",
    "年龄": 20,
    "成绩": [85, 92, 78],
    "专业": "计算机科学"
}

# 2.2 添加新的键值对："班级": "2023级1班"
student_info["班级"] = "2023级1班"

# 2.3 创建一个课程列表
courses = ["Python编程", "数据结构", "算法设计"]

# 2.4 在课程列表中添加"数据库原理"
courses.append("数据库原理")

# 2.5 创建一个元组存储学期信息
semester = ("2023", "秋季")

print("学生信息:", student_info)
print("课程列表:", courses)
print("学期信息:", semester)

print()

# 练习3：条件语句（A.3）
print("练习3：条件语句")
print("-" * 30)

# 3.1 根据成绩判断等级
score = 85

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"成绩 {score} 分，等级: {grade}")

# 3.2 多重条件判断
age = 25
has_ticket = True
has_id = True

if age >= 18 and has_ticket and has_id:
    print("可以进入电影院")
else:
    print("不能进入电影院")

print()

# 练习4：循环语句（A.4）
print("练习4：循环语句")
print("-" * 30)

# 4.1 for循环：计算1-10的和
total = 0
for i in range(1, 11):
    total += i
print(f"1-10的和: {total}")

# 4.2 while循环：猜数字游戏
import random
target = random.randint(1, 10)
guess_count = 0
max_attempts = 3

print("猜数字游戏（1-10），你有3次机会:")

while guess_count < max_attempts:
    guess = int(input(f"第{guess_count + 1}次猜测: "))
    guess_count += 1
    
    if guess == target:
        print("恭喜，猜对了！")
        break
    elif guess < target:
        print("猜小了")
    else:
        print("猜大了")
else:
    print(f"游戏结束，正确答案是: {target}")

# 4.3 列表推导式：生成平方数列表
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"原列表: {numbers}")
print(f"平方列表: {squares}")

print()

# 练习5：函数定义和调用（A.5）
print("练习5：函数定义和调用")
print("-" * 30)

# 5.1 定义一个计算BMI的函数
def calculate_bmi(weight, height):
    """计算BMI指数"""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# 5.2 定义一个带默认参数的函数
def greet_person(name, greeting="你好"):
    """问候函数，有默认问候语"""
    return f"{greeting}，{name}！"

# 5.3 可变参数函数
def calculate_total(*prices):
    """计算任意数量商品的总价"""
    return sum(prices)

# 测试函数
bmi = calculate_bmi(70, 1.75)
print(f"BMI指数: {bmi}")

message1 = greet_person("张三")
message2 = greet_person("李四", "欢迎")
print(message1)
print(message2)

total_price = calculate_total(10, 20, 30, 15)
print(f"商品总价: {total_price}")

print()

# 练习6：模块和包管理（A.6）
print("练习6：模块和包管理")
print("-" * 30)

# 6.1 使用math模块
import math
print(f"圆周率: {math.pi}")
print(f"2的平方根: {math.sqrt(2):.2f}")

# 6.2 使用datetime模块
from datetime import datetime, timedelta
now = datetime.now()
print(f"当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 计算一周后的日期
one_week_later = now + timedelta(days=7)
print(f"一周后: {one_week_later.strftime('%Y-%m-%d')}")

# 6.3 使用random模块
import random
print(f"随机整数(1-100): {random.randint(1, 100)}")

colors = ["红色", "蓝色", "绿色", "黄色"]
print(f"随机颜色: {random.choice(colors)}")

print()

# 综合练习：学生成绩管理系统
print("综合练习：学生成绩管理系统")
print("-" * 40)

def create_student_record(name, scores):
    """创建学生记录"""
    average_score = sum(scores) / len(scores)
    
    if average_score >= 90:
        level = "优秀"
    elif average_score >= 80:
        level = "良好"
    elif average_score >= 70:
        level = "中等"
    elif average_score >= 60:
        level = "及格"
    else:
        level = "不及格"
    
    return {
        "姓名": name,
        "成绩": scores,
        "平均分": round(average_score, 2),
        "等级": level
    }

def print_student_info(students):
    """打印学生信息"""
    for student in students:
        print(f"姓名: {student['姓名']}")
        print(f"成绩: {student['成绩']}")
        print(f"平均分: {student['平均分']}")
        print(f"等级: {student['等级']}")
        print("-" * 20)

# 创建学生记录
students = [
    create_student_record("张三", [85, 92, 78]),
    create_student_record("李四", [95, 88, 91]),
    create_student_record("王五", [65, 72, 68])
]

print_student_info(students)

print("=== 复习练习完成 ===")
print("请检查输出结果，确保所有功能正常工作")
print("如果有不理解的地方，请回顾相应的知识点")