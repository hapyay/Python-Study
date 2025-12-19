# 简单计算器项目
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
        print("
=== 简单计算器 ===")
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
