from pages.basepage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    email_field = (By.ID, "email")
    password_field = (By.ID, "password")
    login_button = (By.ID, 'email_sign_in_button')

    def fill_email(self, email):
        super().type_in(self.email_field, email)

    def fill_password(self, password):
        return super().type_in(self.password_field, password)

    def click_on_login_button(self):
        super().click(self.login_button)
