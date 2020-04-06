# -*- coding: utf-8 -*-
import time
from asyncio import sleep

from test.conftest import Base


class TestJS(Base):
    def test_js_scrool(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")#执行js代码块定位元素，注意要有return的关键字
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")#滑动到最后
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='page']/a[10]").click()#点击下一页
        time.sleep(3)
        # for code in ['return document.title','return JSON.stringify(performance.timing)']:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script("return document.title;JSON.stringify(performance.timing)"))


    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        #self.driver.execute_script("return document.getElementById('train_date')")
        self.driver.execute_script("document.getElementById('train_date').removeAttribute('readonly')")
        #移除只读属性
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-31'")
        #赋值
        sleep(3)