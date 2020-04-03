# -*- coding: utf-8 -*-
import time

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
