from pages.loginpage import LoginPage
from hamcrest import assert_that, equal_to

@given(u'I am on Login Page')
def step_impl(context):
    context.page_object = LoginPage(context.driver)

@when(u'I fill the email "{email}"')
def step_impl(context, email):
    context.page_object.fill_email(email)

@when(u'I fill the fill password "{password}"')
def step_impl(context, password):
    context.page_object.fill_password(password)

@when(u'I click on login button')
def step_impl(context):
    context.page_object.click_on_login_button()
