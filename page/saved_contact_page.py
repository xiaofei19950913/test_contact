import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class SavedContactPage(BaseAction):
    # 获取标题
    contact_title_feature = By.ID, "com.android.contacts:id/large_title"

    @allure.step(title='获取标题')
    def get_contact_title_text(self):
        return self.find_element(self.contact_title_feature).text