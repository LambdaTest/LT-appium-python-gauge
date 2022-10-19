import os
from getgauge.python import before_suite, after_suite
from appium import webdriver
import requests

class Driver(object):
    driver = None

    @before_suite
    def init(self):
        self.username = os.getenv("LT_USERNAME") if os.getenv("LT_USERNAME") is not None else "LT_USERNAME" # replace with your LT username
        self.authkey  = os.getenv("LT_ACCESS_KEY") if os.getenv("LT_ACCESS_KEY") is not None else "LT_ACCESS_KEY" # replace with your LT access key


        caps = {}
        
        # replace with your desired test capabilities
        caps['name'] = 'Gauge Sample Test'
        caps['build'] = 'Python_Gauge_LambdaTest'
        caps['isRealMobile'] = 'true'
        caps['platformVersion'] = '11'
        caps['platform'] = 'Android'
        caps['deviceName'] = 'Galaxy S21 Ultra 5G'
        caps['app'] = 'lt://proverbial-android'      #Enter your app url here


        # start the remote browser on our server
        Driver.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@mobile-hub.lambdatest.com/wd/hub"%(self.username,self.authkey)
         )


    @after_suite
    def close():
        Driver.driver.quit()
