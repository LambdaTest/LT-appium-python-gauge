from sqlite3 import Time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getgauge.python import step
from step_impl.utils.driver import Driver

@step("changes color to pink")
def change_color():
  colorElement = WebDriverWait(Driver.driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/color")))
  colorElement.click()

@step("changes the text to Proverbial")
def chnage_text():
    textElement = WebDriverWait(Driver.driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.lambdatest.proverbial:id/Text")))
    textElement.click()

@step("toast will be visible")
def toast_visible():
    toastElement = WebDriverWait(Driver.driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/toast")))
    toastElement.click()

@step("notification will be visible")
def notification():
  notification = WebDriverWait(Driver.driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/notification")))
  notification.click()

@step("perform the speed test")
def speedTest():
  speedTest = WebDriverWait(Driver.driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/speedTest")))
  speedTest.click()

@step("back to home")
def home():
  home = WebDriverWait(Driver.driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/buttonPage")))
  home.click()