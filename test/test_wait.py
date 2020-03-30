# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://home.testing-studio.com/')
        self.driver.implicitly_wait(3)#隐式等待
    def test_wait(self):
        self.driver.find_element_by_xpath('//*[title="归入各种类别的所有主题"]').click()
        #sleep(3)#直接等待

        def wait(x):#这里一定要定义一个参数，后面until时会将self._driver传递给x
            return len(self.driver.find_element_by_xpath('//*[@class="table-heading"]')) >= 1
        WebDriverWait(self.driver,10).until(wait)#这里是传参，不要写成wait（）
        #WebDriverWait(self.driver,10).until()
        expected_conditions.element_to_be_clickable(By.Xpath, '//*[@class="table-heading"]')#判断这个元素是可被点击的
        self.driver.find_element_by_xpath('//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        print('hello')