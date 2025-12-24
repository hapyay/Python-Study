# 文件操作基础练习
# C.13 文件读写操作

print("=== Python文件操作基础练习 ===")
print("学习目标：掌握文件读写的基本操作")

# 1. 基础文件写入操作
print("\n1. 基础文件写入操作")

# 使用with语句打开文件，这是推荐的方式
# 'w'模式表示写入（write），如果文件不存在会创建，如果存在会覆盖
try:
    with open('test_file.txt', 'w', encoding='utf-8') as file:
        file.write("这是第一行文本\n")
        file.write("这是第二行文本\n")
        file.write("这是第三行文本\n")
    print("✅ 文件写入成功！")
except Exception as e:
    print(f"❌ 文件写入失败: {e}")

# 2. 基础文件读取操作
print("\n2. 基础文件读取操作")

# 'r'模式表示读取（read）
try:
    with open('test_file.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("文件内容：")
        print(content)
    print("✅ 文件读取成功！")
except FileNotFoundError:
    print("❌ 文件不存在，请先运行写入操作")
except Exception as e:
    print(f"❌ 文件读取失败: {e}")

# 3. 逐行读取文件
print("\n3. 逐行读取文件")

try:
    with open('test_file.txt', 'r', encoding='utf-8') as file:
        print("逐行读取内容：")
        for line_num, line in enumerate(file, 1):
            print(f"第{line_num}行: {line.strip()}")
    print("✅ 逐行读取成功！")
except FileNotFoundError:
    print("❌ 文件不存在")

# 4. 追加模式操作
print("\n4. 追加模式操作")

# 'a'模式表示追加（append），在文件末尾添加内容
try:
    with open('test_file.txt', 'a', encoding='utf-8') as file:
        file.write("这是追加的内容\n")
        file.write("这也是追加的内容\n")
    print("✅ 文件追加成功！")
    
    # 读取追加后的内容
    with open('test_file.txt', 'r', encoding='utf-8') as file:
        print("追加后的文件内容：")
        print(file.read())
        
except Exception as e:
    print(f"❌ 文件追加失败: {e}")

print("\n=== 基础文件操作练习完成 ===")
print("请检查输出结果，理解不同文件模式的区别")