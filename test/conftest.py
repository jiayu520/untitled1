# -*- coding: utf-8 -*-
import pytest
# @pytest.fixture()
# def login():
#     print("这是一个登陆方法")

# @pytest.fixture(scope="module")
# def open():
#     print("打开浏览器")
#     yield
#
#     print("执行teardown！")
#     print("最后关闭浏览器")
from selenium import webdriver


class Base:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        pass

    def teardown(self):
        self.driver.quit()
        pass

#
# def pytest_configure(config):
#     maker_list = ["search","login"] #标签名集合
#     for markers in maker_list:
#         config.addinivalue_line(
#             "markers",markers
#         )