# -*- coding: utf-8 -*-
from asyncio import sleep

from selenium import webdriver

from test.conftest import Base


class Testwindows(Base):
    def test_window(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)#当前页面的句柄
        #self.driver.find_element_by_link_text("立刻注册").click()
        self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div/div/div/div/div/div[3]/a").click()
        print(self.driver.window_handles)  # 打印所有句柄，这是有两个句柄，因为有两个窗口了，返回的是一个列表
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])#取列表中的最后一个
        self.driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[2]/form/p[2]/input[2]").send_keys("jiayu")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13800000")#输入手机号
        print(self.driver.window_handles)
        self.driver.switch_to.window(windows[0])#切换为原来的页面
        self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()#点击用户名登录
        self.driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("jiayu")
        self.driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("13888888")
        self.driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
        sleep(3)
