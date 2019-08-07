import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class NewContactPage(BaseAction):

    name_edit_text = By.XPATH, "//*[@text='姓名']"

    phone_edit_text = By.XPATH, "//*[@text='电话']"

    # 新页面 添加联系人的 name phone
    @allure.step(title='输入联系人姓名')
    def input_name(self,name):
        allure.attach("姓名:",name,allure.attach_type.TEXT)
        self.input(self.name_edit_text,name)
        allure.attach("图片:",self.driver.get_screenshot_as_png(),allure.attach_type.PNG)


    @allure.step(title='输入联系人手机号')
    def input_phone(self,phone):
        allure.attach("姓名:", phone, allure.attach_type.TEXT)
        self.input(self.phone_edit_text,phone)
        allure.attach("图片:",self.driver.get_screenshot_as_png(),allure.attach_type.PNG)

