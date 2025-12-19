# 基础语法练习
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
