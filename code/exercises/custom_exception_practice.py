# 自定义异常练习题目
# 请根据题目要求完成代码

# 题目1：创建基础自定义异常
from pickle import Pickler
from unittest import result


class PasswordTooShortError(Exception):
    """
    密码太短异常
    要求：当密码长度小于8个字符时抛出此异常
    异常消息格式："密码长度必须至少8个字符，当前长度：{length}"
    """
    def __init__(self, length) :
        self.length = length
        super().__init__(f"密码长度必须至少8个字符，当前长度：{length}")

# 题目2：创建带额外信息的自定义异常
class EmailFormatError(ValueError):
    """
    邮箱格式错误异常
    要求：
    - 继承自ValueError
    - 携带邮箱地址和错误描述
    - 异常消息格式："邮箱格式错误：{email} - {message}"
    """
    def __init__(self, email,message):
        self.email = email
        self.message = message 
        super().__init__(f"邮箱格式错误：{email} - {message}")
class UsernameFormatError(Exception):
    """
    用户名字符异常
    - 要求：当用户名包含字符时抛出此异常
    """
    def __init__(self,username):
        self.username = username
        super().__init__(f"用户名不能包含符号")
# 题目3：实现用户注册验证函数
def validate_user_registration(username, password, email):
    """
    验证用户注册信息
    要求：
    1. 用户名：长度3-20字符，只能包含字母数字
    2. 密码：长度至少8字符
    3. 邮箱：必须包含@符号
    
    如果验证失败，抛出相应的自定义异常
    """
    name = len(username)
    if name < 3 or name > 20 :
        print(f"用户名太短，当前用户名{name}位")
        return False
    if not username.isalnum():
        raise UsernameFormatError(username)
    if len(password) < 8 :
        raise PasswordTooShortError(len(password))
    if "@" not in email:
        raise EmailFormatError(email, "缺少@符号")
    return True

# 题目4：异常处理测试
def test_validation():
    """
    测试各种验证场景
    要求：捕获不同类型的异常并输出相应信息
    """
    test_cases = [
        ("ab", "123456", "test@example.com"),      # 用户名太短
        ("validuser", "123", "test@example.com"),    # 密码太短
        ("validuser", "12345678", "invalid-email"),  # 邮箱格式错误
        ("validuser", "12345678", "test@example.com") # 有效数据
    ]
    
    for username, password, email in test_cases:
        print(f"\n测试: 用户名='{username}', 密码='{password}', 邮箱='{email}'")
        try:
            result=validate_user_registration(username, password, email )
        except PasswordTooShortError as e:
            print(f"密码错误：{e}")
        except UsernameFormatError as e :
            print(f"用户名错误：{e}")
        except EmailFormatError as e :
            print(f"邮箱错误:{e}")
        except Exception as e :
            print(f"其他错误:{e}")
        else :
            print("验证通过")
        # 你的异常处理代码写在这里
        # 需要分别处理不同类型的异常

# 运行测试
if __name__ == "__main__":
    test_validation()