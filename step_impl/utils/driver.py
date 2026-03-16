import os
from getgauge.python import before_suite, after_suite
from appium import webdriver
from appium.options.android import UiAutomator2Options


class Driver:
    driver = None

    @before_suite
    def init(self):

        username = os.getenv("LT_USERNAME")
        access_key = os.getenv("LT_ACCESS_KEY")

        caps = {
            "platformName": "Android",
            "appium:platformVersion": "13",
            "appium:deviceName": "Galaxy S21 Ultra 5G",
            "appium:app": "lt://proverbial-android",
            "lt:options": {
                "name": "Gauge Sample Test",
                "build": "Python_Gauge_LambdaTest",
                "isRealMobile": True
            }
        }

        options = UiAutomator2Options().load_capabilities(caps)

        hub_url = f"https://{username}:{access_key}@mobile-hub.lambdatest.com/wd/hub"

        print("Starting LambdaTest session...")

        Driver.driver = webdriver.Remote(
            command_executor=hub_url,
            options=options
        )

        print("Session started:", Driver.driver.session_id)

    @after_suite
    def close(self):

        if Driver.driver:
            Driver.driver.quit()