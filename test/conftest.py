# -*- coding: utf-8 -*-
import pytest
# @pytest.fixture()
# def login():
#     print("这是一个登陆方法")

@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield

    print("执行teardown！")
    print("最后关闭浏览器")

def pytest_configure(config):
    maker_list = ["search","login"] #标签名集合
    for markers in maker_list:
        config.addinivalue_line(
            "markers",markers
        )