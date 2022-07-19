import time
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select

url = 'http://10.1.1.22/a70.htm?wlanuserip=172.17.112.29&wlanacip=&wlanacname=&redirect=&session=&vlanid=0&ip=172.17.112.29&mac=000000000000'

#  通过指定chromedriver的路径来实例化driver的对象
driver = webdriver.Chrome()

#  控制浏览器访问url地址
driver.get(url)
print(f'Testing...\ntest url:{url}')
time.sleep(1)

# 定位用户名 输入用户名
driver.find_element_by_id('VipDefaultAccount').send_keys('311041210')
print('Account ready')
time.sleep(0.5)

# 定位密码 输入密码
driver.find_element_by_id('VipDefaultPassword').send_keys('041210')
print('Password ready')
time.sleep(0.5)

# 定位下拉菜单选择电信
select = Select(driver.find_element_by_id('suffixType'))
select.select_by_value('@telecom')
print('Operator: telecom')

# 定位登陆按钮点击
driver.find_element_by_id('login').click()
print('Login button clicked')

# 获取登陆信息
message = driver.find_element_by_id('message').text.replace('\n', ' ')
print(f'Login status message: {message}')

# 判断登陆是否成功
url_test = 'https://www.baidu.com'

if 'AC认证失败' in message:
    print('AC authentication failure,testing whether the network connected')
    res = requests.get(url_test)
    print(f'Test url: {url_test}')
    if res.status_code == 200:
        print(f'Test status code: {res.status_code}')
        print('Network connection successful,do not login repeatedly')
    else:
        print('Network connection failure')
else:
    print('Login successful')

# 退出浏览器
driver.quit()
print('Browser quited')
