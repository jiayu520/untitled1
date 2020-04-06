from asyncio import sleep

from selenium.webdriver.common.by import By

from test.conftest import Base


class TestFile(Base):
    def  test_file_uplod(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("C:\\Users\\Administrator\\PycharmProjects\\untitled1\\baidu.png")
        #上传文件,注意window路径需要转义
        sleep(3)