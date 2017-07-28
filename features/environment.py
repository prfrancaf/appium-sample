from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.example.prff.appiumsample'
desired_caps['appActivity'] = 'com.example.prff.appiumsample.LoginActivity'

def before_feature(context, feature):
    context.driver = webdriver.Remote(context.config.userdata['appiumServerUrl'], desired_caps)
