# 模块和包管理演示

# 示例1：导入整个模块
import math
import random
import datetime
import os

# 示例2：从模块导入特定功能
from math import sqrt, pi, sin, cos
from random import randint, choice
from datetime import date, datetime, timedelta

# 示例3：给模块起别名
import math as m
import random as rnd

# 示例4：导入模块中的所有功能（不推荐，容易命名冲突）
# from math import *

print("=== 示例1：使用math模块 ===")
print(f"π的值: {math.pi}")
print(f"2的平方根: {math.sqrt(2)}")
print(f"sin(90°): {math.sin(math.pi/2)}")

print("\n=== 示例2：使用random模块 ===")
print(f"随机整数(1-100): {random.randint(1, 100)}")
print(f"随机小数(0-1): {random.random()}")
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(f"随机选择水果: {random.choice(fruits)}")

print("\n=== 示例3：使用datetime模块 ===")
today = datetime.now()
print(f"当前时间: {today}")
print(f"格式化时间: {today.strftime('%Y年%m月%d日 %H:%M:%S')}")

# 计算未来日期
future_date = today + timedelta(days=7)
print(f"一周后的日期: {future_date.strftime('%Y-%m-%d')}")

print("\n=== 示例4：使用os模块 ===")
print(f"当前工作目录: {os.getcwd()}")
print(f"操作系统类型: {os.name}")

# 示例5：创建和使用自定义模块
# 首先创建一个简单的自定义模块文件：my_utils.py

# 假设my_utils.py文件内容如下：
"""
# my_utils.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(number):
    return number % 2 == 0

def greet(name):
    return f"你好，{name}！"
"""

# 在实际项目中，我们会这样导入自定义模块：
# from my_utils import add, multiply, is_even, greet

# 这里我们直接定义这些函数来演示
class MyUtils:
    """模拟自定义模块的功能"""
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    
    @staticmethod
    def greet(name):
        return f"你好，{name}！"

print("\n=== 示例5：使用自定义模块（模拟） ===")
print(f"5 + 3 = {MyUtils.add(5, 3)}")
print(f"4 × 6 = {MyUtils.multiply(4, 6)}")
print(f"7是偶数吗？ {MyUtils.is_even(7)}")
print(MyUtils.greet("张三"))

print("\n=== 示例6：常用标准库模块介绍 ===")

# 数学相关模块
print("数学模块:")
print("- math: 数学函数（三角函数、对数、常数等）")
print("- random: 随机数生成")
print("- statistics: 统计计算")

# 日期时间模块
print("\n日期时间模块:")
print("- datetime: 日期和时间处理")
print("- time: 时间相关功能")
print("- calendar: 日历功能")

# 文件系统模块
print("\n文件系统模块:")
print("- os: 操作系统接口")
print("- sys: 系统相关参数和函数")
print("- pathlib: 面向对象的文件系统路径")

# 数据处理模块
print("\n数据处理模块:")
print("- json: JSON编码和解码")
print("- csv: CSV文件读写")
print("- re: 正则表达式")

# 网络和网络模块
print("\n网络相关模块:")
print("- urllib: URL处理")
print("- requests: HTTP请求（第三方库）")
print("- socket: 网络通信")

print("\n=== 示例7：模块的属性和方法查看 ===")

# 查看模块的可用功能
print("math模块的部分功能:")
math_functions = [func for func in dir(math) if not func.startswith('_')]
print(math_functions[:10])  # 显示前10个功能

# 查看模块文档
print("\nmath模块的文档:")
print(math.__doc__[:200] + "...")  # 显示前200个字符

print("\n=== 模块演示完成 ===")

# 示例8：包的概念演示
print("\n=== 示例8：包的概念 ===")
print("""
包（Package）是包含多个模块的目录，具有以下特点：

1. 包含__init__.py文件（Python 3.3+可以省略）
2. 可以包含子包（子目录）
3. 使用点号表示法访问：package.subpackage.module

示例包结构：
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py

导入方式：
import my_package.module1
from my_package.subpackage import module3
""")