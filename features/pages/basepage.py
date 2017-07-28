from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.wait_for(EC.element_to_be_clickable(locator)).click()

    def find(self, locator):
        element = self.wait_for(EC.visibility_of_element_located(locator))
        return element

    def wait_for(self,condition, seconds = 5):
        return  WebDriverWait(self.driver,seconds).until(condition)

    def type_in(self,locator,text,set_clear = True):
        element= self.find(locator)
        if set_clear:
            element.clear()
        element.send_keys(text)
