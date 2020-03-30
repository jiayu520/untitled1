from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")#by表示用什么方法定位，send_keys表示输入内容
        self.driver.find_element(By.ID,'su').click()
