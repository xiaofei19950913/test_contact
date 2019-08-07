import time
import pytest
import yaml
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestContact:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 参数化 需要传两个值 参数文件,执行函数名
    # @pytest.allure.serverity(pytest.allure.serverity_level.BLOCKER)
    @pytest.mark.parametrize("args", analyze_file("contact_data.yaml", "test_contact"))
    def test_contact(self,args):

        name = args["name"]
        phone = args["phone"]
        self.page.contact_list.click_add_contact()
        self.page.new_contact.input_name(name)
        self.page.new_contact.input_phone(phone)

        # 点击返回=保存
        self.page.new_contact.press_back()
        # 断言,保存好的页面的名字是否和传进去的值相同
        assert name == self.page.saved_contact.get_contact_title_text()