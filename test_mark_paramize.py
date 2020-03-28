import sys

import pytest

#参数化 ,前两个是变量,后面是对应的数据
#3+5->test_input 8->expect
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",30)])
def test_eval(test_input,expected):
    #eval 将字符串str当成有效的表达式来求值，并返回结果
    assert  eval(test_input) == expected