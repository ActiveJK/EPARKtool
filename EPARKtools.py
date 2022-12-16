from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import datetime
import sys


'''------------------以下に各情報を入力----------------------------'''
mail = ''
passwd = ''
telephone = ''
target_shop_url = ''
set_time = datetime.time(5, 4, 00) #時間入力(h, m, s)
'''-------------------------------------------------------------'''


options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('C:\Doc\chromedriver_win32\chromedriver', options=options)
driver.get('https://v1-account.epark.jp/auth?client_id=epark_faspa&redirect_uri=https%3A%2F%2Fepark.jp%2Fv2auth&state=UPjCsS4CvRVBn8MknPsFj0lDP433Yu2yvudgn00c&new_mem_back_uri=https%3A%2F%2Fepark.jp%2F')


mail_box = driver.find_element_by_name('auth_login[username]')
pass_box = driver.find_element_by_name('auth_login[password]')

mail_box.send_keys(mail)
pass_box.send_keys(passwd)
mail_box.submit()

cont = 0
while True:
    get_time = datetime.datetime.now().time()
    if get_time >= set_time:
        driver.get(target_shop_url)

    try:
        driver.find_element_by_xpath('//*[@id="shopdata-main"]/div[2]/div[4]/aside/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/button').click()
        break
    except NoSuchElementException:
        if cont < 3:
            cont += 1
        else:
            sys.exit()

driver.find_element_by_xpath('//*[@id="receive_shop_reserve_category_value_3"]').send_keys(telephone)
driver.find_element_by_class_name('btn_submit').submit()
driver.find_element_by_class_name('btn_submit').submit()
