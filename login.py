# -- coding: utf-8 --
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

def login(driver,account,passward):
    driver.implicitly_wait(10)  # 设置全局最大等待时间
    driver.find_element_by_id("com.cditv.whxxapp:id/main_login_user_name").send_keys(account)
    driver.find_element_by_id("com.cditv.whxxapp:id/main_login_pwd").send_keys(passward)
    driver.find_element_by_id("com.cditv.whxxapp:id/main_login_submit").click()
    #设置等待时间
    if WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id("com.cditv.whxxapp:id/data_year_tv")):
        return "登录成功"
    else:
        return "登录失败"
