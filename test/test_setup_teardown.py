# -*- coding: utf-8 -*-
import pytest

def setup_module():
    print("这是个setup_module方法")

def teardown_module():
    print("这是teardown_down方法")

def setup_function():
    print("setup_function")

def teardown_function():
    print("teardown_function")

def test_login():
    print("这是一个外部的方法")
class TestDemo():
    def setup_class(self):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def setup(self):
        print("setup")

    def teardown_class(self):
        print("teardown_class")

    def teardown_method(self):
        print("teardown_method")

    def teardown(self):
        print("teardown")

    def test_a(self):
        print("开始执行test__a方法")
        x = 'this'
        assert 'h' in x

    def test_b(self):
        print("开始执行 test_b 方法")
        x = 'hello'
        assert 'e' in x

    def test_c(self):
        print("开始执行 test_c 方法")
        a = 'hello'
        b = 'hello world'
        assert a in b

if __name__ == '__main__':
        pytest.main("-v -s")