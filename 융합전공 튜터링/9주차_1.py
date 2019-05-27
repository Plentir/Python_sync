from selenium import webdriver as wd
import pandas as pd
from os import environ


rq_header = {
    "User-Agent" : ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.134 Safari/537.36 Vivaldi/2.5.1525.40")
}

dir = environ["USERPROFILE"] + "\\" + "chromedriver.exe"

driver = wd.Chrome(dir)

url = "http://saint.ssu.ac.kr/irj/portal"

driver.implicitly_wait(3)  # 3초 대기시켜주는 거.
driver.get(url)  # URL 호출


id = "20182827"
driver.find_element_by_name("j_username").send_keys(id)

pw = "yjy990810?"
driver.find_element_by_name("j_password").send_keys(pw)

driver.find_element_by_xpath("//*[@id='container']/div[1]/div[1]/div/div[1]/table/tbody/tr[1]/td[3]").click()  # 로그인 버튼 클릭

#driver.find_element_by_xpath("//*[@id='frmNIDLogin']/fieldset/input").click()

driver.implicitly_wait(600)
