# 函数练习
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
