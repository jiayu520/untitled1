# -*- coding: utf-8 -*-
import pytest


class TestDemo():


    def test_one(self):
        print("开始执行test__one方法")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("开始执行 test_two 方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行 test_three 方法")
        a = 'hello'
        b = 'hello world'
        assert a not in b

class TestDemo2():
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
        assert a not in b

if __name__ == '__main__':
            pytest.main()
