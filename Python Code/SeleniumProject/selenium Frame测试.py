import time
from selenium import webdriver

url = 'https://qzone.qq.com/'

driver = webdriver.Chrome()

driver.get(url)

driver.switch_to_frame('login_frame')

driver.find_element_by_id('switcher_plogin').click()

driver.find_element_by_id('u').send_keys('2860874824')
driver.find_element_by_id('p').send_keys('wone988321')
driver.find_element_by_id('login_button').click()

# time.sleep(3)

# shuoshuo = driver.find_elements_by_xpath("//li[@class='feed_page_container']")
# shuo = shuoshuo[0].text
# s_list = shuo.split('评论')
# for s in s_list:
#     s = s.replace('  ','')
#     print(s)
#     print('='*50)


time.sleep(3)

driver.quit()
