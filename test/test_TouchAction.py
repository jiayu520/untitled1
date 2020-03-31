# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        #option = webdriver.ChromeOptions()
        #option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com")
        el = self.driver.find_element_by_id("kw")#定位到输入框
        el_search = self.driver.find_element_by_id("su")#定位到百度一下
        el.send_keys("selenium测试")#输入
        action = TouchActions(self.driver)
        action.tap(el_search)#点击
        action.scroll_from_element(el,0,10000)#从搜索框这个元素开始向下滑动
        action.perform()
        sleep(3)