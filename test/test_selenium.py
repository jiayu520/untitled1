from  selenium import webdriver
from time import  sleep
# def test_selenium():
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com/")
class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()#启动插件
        self.driver.maximize_window()#浏览器最大化
        self.driver.implicitly_wait(10)#隐式 等待
        pass

    def teardown(self):
        self.driver.quit()#退出浏览器
        pass

    def test_hogwars(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
        self.driver.find_element_by_css_selector(".topic-22287 .title > a").click()
        pass