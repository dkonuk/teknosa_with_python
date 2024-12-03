from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def find_element(self, element):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(element))

    def click_element(self, element):
        self.find_element(element).click()

    def find_elements(self, element):
        return self.driver.find_elements(*element)

    def send_keys(self, element, text):
        self.find_element(element).send_keys(text)

    def get_children_of_parent_element(self, element):
        element_list = self.find_elements(element)
        return element_list



