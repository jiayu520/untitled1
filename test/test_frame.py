# -*- coding: utf-8 -*-
from test.conftest import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")#切换到frame
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.parent_frame()#切换回主页面
        #self.driver.switch_to.default_content()#切换回主页面，和上面的是两种方式
        self.driver.find_element_by_id("submitBTN").text