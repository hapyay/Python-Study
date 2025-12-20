# 函数定义和调用演示

# 示例1：最简单的函数（无参数，无返回值）
def say_hello():
    """这是一个简单的问候函数"""
    print("你好！欢迎学习Python函数！")

# 示例2：带参数的函数
def greet(name):
    """带参数的问候函数"""
    print(f"你好，{name}！")

# 示例3：带返回值的函数
def add_numbers(a, b):
    """计算两个数的和并返回结果"""
    result = a + b
    return result

# 示例4：带默认参数的函数
def calculate_area(length, width=10):
    """计算面积，宽度有默认值"""
    area = length * width
    return area

# 示例5：返回多个值的函数
def get_circle_info(radius):
    """计算圆的面积和周长"""
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference  # 返回元组

# 示例6：可变参数函数
def calculate_average(*numbers):
    """计算任意数量数字的平均值"""
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

# 示例7：关键字参数函数
def create_person_info(**info):
    """创建个人信息字典"""
    person = {}
    for key, value in info.items():
        person[key] = value
    return person

# 示例8：函数嵌套调用
def is_even(number):
    """判断是否为偶数"""
    return number % 2 == 0

def filter_even_numbers(numbers):
    """过滤出偶数"""
    even_numbers = []
    for num in numbers:
        if is_even(num):  # 调用另一个函数
            even_numbers.append(num)
    return even_numbers

# 示例9：递归函数
def factorial(n):
    """计算阶乘（递归实现）"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # 递归调用

# 示例10：lambda函数（匿名函数）
# lambda函数是简单的单行函数
square = lambda x: x ** 2
is_adult = lambda age: age >= 18

# 函数调用演示
print("=== 示例1：简单函数调用 ===")
say_hello()

print("\n=== 示例2：带参数的函数 ===")
greet("张三")
greet("李四")

print("\n=== 示例3：带返回值的函数 ===")
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

print("\n=== 示例4：默认参数函数 ===")
area1 = calculate_area(5)      # 使用默认宽度10
area2 = calculate_area(5, 8)   # 指定宽度8
print(f"面积1: {area1}")
print(f"面积2: {area2}")

print("\n=== 示例5：返回多个值 ===")
circle_area, circle_circumference = get_circle_info(5)
print(f"半径为5的圆：面积={circle_area:.2f}, 周长={circle_circumference:.2f}")

print("\n=== 示例6：可变参数函数 ===")
avg1 = calculate_average(1, 2, 3)
avg2 = calculate_average(10, 20, 30, 40, 50)
print(f"平均值1: {avg1}")
print(f"平均值2: {avg2}")

print("\n=== 示例7：关键字参数函数 ===")
person1 = create_person_info(name="王五", age=25, city="北京")
person2 = create_person_info(name="赵六", occupation="工程师")
print(f"人物1: {person1}")
print(f"人物2: {person2}")

print("\n=== 示例8：函数嵌套调用 ===")
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = filter_even_numbers(numbers_list)
print(f"原列表: {numbers_list}")
print(f"偶数列表: {even_list}")

print("\n=== 示例9：递归函数 ===")
factorial_5 = factorial(5)
print(f"5的阶乘: {factorial_5}")

print("\n=== 示例10：lambda函数 ===")
print(f"5的平方: {square(5)}")
print(f"20岁是否成年: {is_adult(20)}")

print("\n=== 函数演示完成 ===")

# 函数文档字符串演示
print("\n=== 函数文档字符串 ===")
print("add_numbers函数的文档:")
print(add_numbers.__doc__)

# 查看函数信息
print("\n=== 函数信息 ===")
print(f"函数名: {add_numbers.__name__}")
print(f"模块名: {add_numbers.__module__}")