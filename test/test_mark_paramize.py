import sys

import pytest

#参数化 ,前两个是变量,后面是对应的数据
#3+5->test_input 8->expect
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",30)])
def test_eval(test_input,expected):
    #eval 将字符串str当成有效的表达式来求值，并返回结果
    assert  eval(test_input) == expected

#参数组合
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[8,10])
def  test_foo(x,y):
    print(f"测试数据组合x: {x},y:{y}")
    print("测试数据组合x: %d"  "y:%d"  %(x,y))

#方法名作为参数
test_user_data = ['Tom', 'Jerry']
@pytest.fixture(scope="module")
def login_r(request):
    #这是接收并传入的参数
    user = request.param
    print(f"\n 打开首页准备登陆，登陆用户名：{user}")
    return user
@pytest.mark.skip(sys.platform  == "darwin",reason="不在Mac上执行，此次测试不执行")
#添加一些跳过的条件
#indirect=True,可以传过来的参数当函数来执行
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中 login 的返回值：{a}")
    assert a != ""

if __name__ == '__main__':
    pytest.main('-v')