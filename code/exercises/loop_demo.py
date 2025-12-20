# 循环语句演示

# 示例1：for循环遍历列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("=== 示例1：for循环遍历列表 ===")
print("水果列表:")
for fruit in fruits:
    print(f"- {fruit}")

# 示例2：for循环遍历字符串
word = "Python"
print("\n=== 示例2：for循环遍历字符串 ===")
print("字母分解:")
for letter in word:
    print(letter)

# 示例3：for循环使用range()函数
print("\n=== 示例3：for循环使用range()函数 ===")
print("数字1-5:")
for i in range(1, 6):
    print(i)

# 示例4：while循环基础
count = 1
print("\n=== 示例4：while循环基础 ===")
print("while循环示例:")
while count <= 5:
    print(f"计数: {count}")
    count += 1  # 重要：必须更新计数器，否则会无限循环

# 示例5：continue语句
print("\n=== 示例5：continue语句 ===")
print("打印1-10中的奇数:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i)

# 示例6：嵌套循环
print("\n=== 示例6：嵌套循环 ===")
print("乘法表（1-3）:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}", end="\t")
    print()  # 换行

# 示例7：循环与列表推导式
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # 列表推导式
print("\n=== 示例7：循环与列表推导式 ===")
print(f"原列表: {numbers}")
print(f"平方列表: {squares}")

print("\n=== 循环演示完成 ===")