# -- coding: utf-8 --
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def logout(driver):
    driver.implicitly_wait(10)  # 设置全局最大等待时间
    driver.find_element_by_name("我的").click()
    driver.find_element_by_id("com.cditv.whxxapp:id/main_tv_logout").click()
    driver.find_element_by_id("android:id/button1").click()
    # 设置等待时间
    if WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id("com.cditv.whxxapp:id/main_login_submit")):
        return "退出成功"
    else:
        return "退出失败"