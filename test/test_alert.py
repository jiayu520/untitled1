from asyncio import sleep

from selenium.webdriver import ActionChains

from test.conftest import Base


class TestAkert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")#切换到frame页面
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action= ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()#拖拽
        sleep(5)
        self.driver.switch_to.alert.accept()#点击alert上的确认
        self.driver.switch_to.default_content()#切换回默认页面
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)

