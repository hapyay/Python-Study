# 创建Python学习项目目录结构
import os

def create_project_structure():
    """创建Python学习项目的目录结构"""
    
    # 基础目录结构
    base_dirs = [
        'code/exercises',
        'code/projects', 
        'code/solutions',
        'code/tests'
    ]
    
    print("正在创建Python学习项目目录结构...")
    
    for dir_path in base_dirs:
        full_path = os.path.join(os.path.dirname(__file__), dir_path)
        os.makedirs(full_path, exist_ok=True)
        print(f"✓ 创建目录: {dir_path}")
    
    # 创建基础练习文件
    exercise_files = {
        'code/exercises/basic_syntax.py': '''# 基础语法练习
# 变量和数据类型练习

# 1. 基本数据类型
name = "Python学习者"
age = 25
height = 175.5
is_student = True

# 2. 列表练习
numbers = [1, 2, 3, 4, 5]
fruits = ["苹果", "香蕉", "橙子"]

# 3. 字典练习
person = {
    "name": "张三",
    "age": 30,
    "city": "北京"
}

# 4. 条件语句练习
def check_age(age):
    if age >= 18:
        return "成年人"
    else:
        return "未成年人"

# 测试代码
if __name__ == "__main__":
    print(f"姓名: {name}")
    print(f"年龄检查: {check_age(age)}")
    print(f"水果列表: {fruits}")
''',
        
        'code/exercises/data_structures.py': '''# 数据结构练习
# 列表、元组、字典、集合的用法

# 列表操作
def list_operations():
    my_list = [1, 2, 3, 4, 5]
    # 添加元素
    my_list.append(6)
    # 删除元素
    my_list.remove(3)
    # 切片操作
    sliced = my_list[1:4]
    return my_list, sliced

# 元组练习
def tuple_example():
    coordinates = (10, 20)
    # 元组解包
    x, y = coordinates
    return x, y

# 字典操作
def dict_operations():
    student = {"name": "李四", "score": 85}
    # 添加键值对
    student["grade"] = "A"
    # 遍历字典
    for key, value in student.items():
        print(f"{key}: {value}")
    return student

# 集合练习
def set_operations():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    # 并集
    union = set1 | set2
    # 交集
    intersection = set1 & set2
    return union, intersection

if __name__ == "__main__":
    print("数据结构练习开始...")
''',
        
        'code/exercises/functions.py': '''# 函数练习
# 函数定义、参数传递、返回值

def greet(name, greeting="你好"):
    """简单的问候函数"""
    return f"{greeting}, {name}!"

def calculate_area(length, width):
    """计算矩形面积"""
    return length * width

def is_even(number):
    """判断数字是否为偶数"""
    return number % 2 == 0

def factorial(n):
    """计算阶乘（递归示例）"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def process_numbers(numbers, operation):
    """处理数字列表"""
    if operation == "sum":
        return sum(numbers)
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)
    else:
        return "未知操作"

if __name__ == "__main__":
    # 测试函数
    print(greet("世界"))
    print(f"面积: {calculate_area(5, 3)}")
    print(f"10是偶数吗: {is_even(10)}")
    print(f"5的阶乘: {factorial(5)}")
''',
        
        'code/projects/calculator.py': '''# 简单计算器项目
# 实现基本的四则运算

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            return "错误：除数不能为零"
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def show_history(self):
        """显示计算历史"""
        if not self.history:
            print("暂无计算历史")
        else:
            print("计算历史:")
            for operation in self.history:
                print(f"  {operation}")

def main():
    calc = Calculator()
    
    while True:
        print("\n=== 简单计算器 ===")
        print("1. 加法")
        print("2. 减法") 
        print("3. 乘法")
        print("4. 除法")
        print("5. 查看历史")
        print("6. 退出")
        
        choice = input("请选择操作 (1-6): ")
        
        if choice == '6':
            print("感谢使用计算器！")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("输入第一个数字: "))
                num2 = float(input("输入第二个数字: "))
                
                if choice == '1':
                    result = calc.add(num1, num2)
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                elif choice == '4':
                    result = calc.divide(num1, num2)
                
                print(f"结果: {result}")
                
            except ValueError:
                print("错误：请输入有效的数字")
            except Exception as e:
                print(f"错误：{e}")
        
        elif choice == '5':
            calc.show_history()
        
        else:
            print("无效选择，请重试")

if __name__ == "__main__":
    main()
''',
        
        'code/projects/data_processor.py': '''# 数据处理项目
# 文件读写和数据处理练习

import csv
import json
from datetime import datetime

class DataProcessor:
    def __init__(self):
        self.data = []
    
    def read_csv(self, filename):
        """读取CSV文件"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = list(reader)
            print(f"成功读取 {len(self.data)} 条数据")
            return True
        except FileNotFoundError:
            print(f"文件 {filename} 不存在")
            return False
    
    def process_data(self):
        """处理数据"""
        if not self.data:
            print("没有数据可处理")
            return
        
        # 简单的数据处理示例
        processed = []
        for item in self.data:
            # 这里可以根据实际数据结构进行处理
            processed_item = {**item, "processed_at": datetime.now().isoformat()}
            processed.append(processed_item)
        
        return processed
    
    def save_json(self, data, filename):
        """保存为JSON文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print(f"数据已保存到 {filename}")
            return True
        except Exception as e:
            print(f"保存失败: {e}")
            return False

def create_sample_csv():
    """创建示例CSV文件"""
    sample_data = [
        {"name": "张三", "age": "25", "city": "北京"},
        {"name": "李四", "age": "30", "city": "上海"},
        {"name": "王五", "age": "28", "city": "广州"}
    ]
    
    with open('sample_data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerows(sample_data)
    
    print("已创建示例文件: sample_data.csv")

if __name__ == "__main__":
    processor = DataProcessor()
    
    # 创建示例文件
    create_sample_csv()
    
    # 处理数据
    if processor.read_csv('sample_data.csv'):
        processed_data = processor.process_data()
        processor.save_json(processed_data, 'processed_data.json')
''',
        
        'code/README.md': '''# Python学习代码库

这个目录包含Python学习过程中的所有代码练习和项目。

## 目录结构

- `exercises/` - 基础练习代码
  - `basic_syntax.py` - 基础语法练习
  - `data_structures.py` - 数据结构练习
  - `functions.py` - 函数练习

- `projects/` - 完整项目实践
  - `calculator.py` - 计算器项目
  - `data_processor.py` - 数据处理项目

- `solutions/` - 参考答案和最佳实践
- `tests/` - 单元测试和代码验证

## 使用说明

1. 按照学习计划逐步完成练习
2. 每个主题完成后在相应文件中添加代码
3. 定期提交代码到Git进行版本控制
4. 遇到问题时参考solutions目录中的示例

## 学习建议

- 先理解概念，再动手编码
- 多写注释，便于复习
- 定期回顾已学内容
- 尝试修改和扩展示例代码
'''
    }
    
    # 创建文件
    for file_path, content in exercise_files.items():
        full_path = os.path.join(os.path.dirname(__file__), file_path)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ 创建文件: {file_path}")
    
    print("\n项目结构创建完成！")
    print("现在可以开始你的Python学习之旅了！")

if __name__ == "__main__":
    create_project_structure()
