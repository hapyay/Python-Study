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

# 条件语句示例
# 示例1：基本的if-else结构
price = 15
discount = 0

if price == 10:
    discount = 2
elif price == 15:
    discount = 3
elif price == 18:
    discount = 4
else:
    discount = 0

final_price = price - discount
print(f"原价: {price}, 折扣: {discount}, 最终价格: {final_price}")

# 示例2：多条件判断
temperature = 28
if temperature > 30:
    print("天气炎热，注意防暑")
elif 20 <= temperature <= 30:
    print("天气适宜，适合外出")
else:
    print("天气较冷，注意保暖")

# 示例3：使用and/or组合条件
age = 25
has_id = True
if age >= 18 and has_id:
    print("可以进入")
else:
    print("不能进入")

# 示例4：if嵌套
number = 10
if number > 0:
    if number % 2 == 0:
        print("这是一个正偶数")
    else:
        print("这是一个正奇数")
else:
    print("这不是一个正数")

# 循环语句示例
# 示例1：for循环遍历列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("水果列表:")
for fruit in fruits:
    print(f"- {fruit}")

# 示例2：for循环遍历字符串
word = "Python"
print("\n字母分解:")
for letter in word:
    print(letter)

# 示例3：for循环使用range()函数
print("\n数字1-5:")
for i in range(1, 6):
    print(i)

# 示例4：while循环基础
count = 1
print("\nwhile循环示例:")
while count <= 5:
    print(f"计数: {count}")
    count += 1  # 重要：必须更新计数器，否则会无限循环

# 示例5：无限循环和break
print("\n猜数字游戏（输入0退出）:")
while True:
    number = int(input("请输入一个数字: "))
    if number == 0:
        print("游戏结束")
        break  # 跳出循环
    elif number > 10:
        print("数字太大了")
    elif number < 5:
        print("数字太小了")
    else:
        print("猜对了！")

# 示例6：continue语句
print("\n打印1-10中的奇数:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i)

# 示例7：嵌套循环
print("\n乘法表（1-3）:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}", end="\t")
    print()  # 换行

# 示例8：循环与列表推导式
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # 列表推导式
print(f"\n原列表: {numbers}")
print(f"平方列表: {squares}")

# 测试代码
if __name__ == "__main__":
    print(f"姓名: {name}")
    print(f"年龄检查: {check_age(age)}")
    print(f"水果列表: {fruits}")
