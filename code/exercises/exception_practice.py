# 异常处理练习
# 请完成以下练习

# 练习1：基本的异常处理
def divide_numbers(a, b):
    """
    实现一个安全的除法函数
    如果除数为0，捕获ZeroDivisionError并返回None
    """
    try:
        result1 = a / b
    except ZeroDivisionError:
        print("不能除以0!")
        return None
    else:
        return result1

# 练习2：文件操作异常处理
def read_file_safely(filename):
    """
    安全地读取文件内容
    处理FileNotFoundError和PermissionError
    如果文件不存在，返回"文件不存在"
    如果权限不足，返回"权限不足"
    读取成功返回文件内容
    """
    try:
        with open(filename,"r") as f:
            content = f.read()
    except FileNotFoundError:
        print("文件不存在")
        return "文件不存在"
    except PermissionError:
        print("权限不足")
        return "权限不足"
    else:
        return content

# 练习3：类型转换异常
def safe_int_conversion(text):
    """
    安全地将字符串转换为整数
    如果转换失败，返回None
    """
    try :
        num = int(text)
        
    except ValueError:
        print("无法将字符串转换为数字")
        return None
    else:
        return num

# 测试代码
if __name__ == "__main__":
    # 测试练习1
    print("=== 练习1测试 ===")
    result1 = divide_numbers(10, 2)
    print(f"10 / 2 = {result1}")
    
    result2 = divide_numbers(10, 0)
    print(f"10 / 0 = {result2}")
    
    # 测试练习2
    print("\n=== 练习2测试 ===")
    content = read_file_safely("test.txt")
    print(f"文件内容: {content}")
    
    # 测试练习3
    print("\n=== 练习3测试 ===")
    num1 = safe_int_conversion("123")
    print(f"'123' 转换为整数: {num1}")
    
    num2 = safe_int_conversion("abc")
    print(f"'abc' 转换为整数: {num2}")