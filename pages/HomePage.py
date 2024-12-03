from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from utilities.testdata import testData
import time


class HomePage(BasePage):
    promotions_banner = (By.CSS_SELECTOR, "div.tekno-slide")
    promotions_banner_next_button = (By.CSS_SELECTOR, 'button[class="tekno-next"]')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(testData.url)

    def check_page_title(self):
        return self.get_page_title()

    def check_promotions_banner(self):
        return self.find_elements(self.promotions_banner)

    def check_promotions_banner_text(self):
        self.get_children_of_parent_element(self.promotions_banner)
        for i in range(len(self.get_children_of_parent_element(self.promotions_banner))):
            self.click_element(self.promotions_banner_next_button)
            time.sleep(1)
