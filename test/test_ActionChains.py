# -*- coding: utf-8 -*-
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        #self.driver.get("http://sahitest.com/demo/clicks.htm")
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip#跳过test_case_click
    def test_case_click(self):
        #self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclickclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclickclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        actions = ActionChains(self.driver)
        actions.click(element_click)#单击操作
        actions.context_click(element_rightclickclick)#右键
        actions.double_click(element_doubleclickclick)#双击
        sleep(3)
        actions.perform()#执行action
        sleep(3)
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)#移动鼠标
        action.perform()
        sleep(10)

    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")#定位拖的元素
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")#定位目的元素，拖到哪里
        action = ActionChains(self.driver)
        #action.drag_and_drop(drag_element,drop_element).perform()#从drag_element拖到drop_element
        #action.click_and_hold(drag_element).release(drop_element).perform()#点击并拖住drag_element,拖到drop_element释放
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()#可以达到上面同样的效果
        sleep(3)
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        action = ActionChains(self.driver)
        action.move_to_element(ele).click()#移动到ele并且点击
        action.send_keys("username").pause(1)#输入username，暂停一秒
        action.send_keys(Keys.SPACE).pause(1)#空格
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()#回格
        sleep(3)
if __name__ == '__main__':
    pytest.main()