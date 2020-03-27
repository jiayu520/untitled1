# -*- coding: utf-8 -*-
import pytest


def test_casel(login):
    print("test_case1,要登陆")
    pass
def test_case2():
    print("test_case2，不需要登陆")
    pass
def test_case3(login):
    print("test_case3，不需要登陆")
    pass
if __name__ == '__main__':
    pytest.main()