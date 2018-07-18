# -- coding: utf-8 --
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import login,logout

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.cditv.whxxapp'
desired_caps['appActivity'] = 'com.cditv.whxx.main.ui.act.WelcomeActivity'

def main():

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print login.login(driver,"15301123456","123456")
    print logout.logout(driver)




if __name__ == "__main__":
    main()