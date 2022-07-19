from selenium import webdriver
import time

url = 'http://acac.fanya.chaoxing.com/portal'

driver = webdriver.Chrome()

# 进入学校学习网站
driver.get(url)

# 点击用户登录
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/ul/li[1]/input').click()

# 输入账号密码
driver.find_element_by_id('unameId').send_keys('202001020129')
print('"Account Input Completed"')
time.sleep(0.5)
driver.find_element_by_id('passwordId').send_keys('wc988321')
print('"Password Input Completed"')

# 手动输入验证码
name_code = input('"Please manualInput verificationCode":')
driver.find_element_by_id('numcode').send_keys(name_code)

# 点击登录
driver.find_element_by_xpath('//*[@id="form"]/table/tbody/tr[7]/td[2]/label/input').click()
time.sleep(1)

# 点击在线学习
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/a').click()
time.sleep(1)

# 进入新标签页代码
windows = driver.window_handles
driver.switch_to_window(windows[1])

# 进入iframe课程页面
driver.switch_to_frame('frame_content')
time.sleep(1)

# 拿到课程标签
Course_list = driver.find_elements_by_xpath('//html/body/div/div[2]/div[3]/ul/li/div[2]/h3/a')
Course_list_url = []

# 选择课程
index = 0
print('-=-'*20)
for Course in Course_list:
    print(f'{index + 1}. Course: {Course.text}')
    Course_list_url.append(Course.get_attribute('href'))
    index += 1
print('-=-'*20)

select = int(input('"Please Select Course Number":'))

Course_url = Course_list_url[select - 1]
print(f'| Course: {Course_list[select - 1].text} | url: {Course_url} |')

# 进入课程页面
driver.get(Course_url)
# print(driver.window_handles)

# 获取每个任务点
chapter_list = driver.find_elements_by_xpath('//em')

# 获取每个任务点的状态
chapter_status = []
for chapter in chapter_list:
    chapter = chapter.get_attribute('class')
    chapter_status.append(chapter)

orange = 0
blank = 0
openlock = 0

for status in chapter_status:
    if status == 'orange':
        orange += 1
    elif status == 'blank':
        blank += 1
    elif status == 'openlock':
        openlock += 1

if orange == 0 and blank == 0 and openlock > 0:
    print('"You Finished This Course"')
if orange > 0 or blank > 0 :
    unfinished = orange + blank
    print(f'"You Finished {openlock} Chapter And You Have {unfinished} Chapter Unfinished, Please Complete Them"')


time.sleep(3)
driver.quit()
