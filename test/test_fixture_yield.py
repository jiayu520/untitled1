# -*- coding: utf-8 -*-
import pytest


def test_search1(open):
    print("test_search1")
    raise NameError
    pass

def test_search2(open):
    print("test_sarch2")
    pass

def  test_search3(open):
    print("test_search")
    pass

if __name__ == '__main__':
    pytest.main()
