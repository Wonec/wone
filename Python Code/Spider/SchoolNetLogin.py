import requests

class SchoolNetLogin:
    def __init__(self):

        self.url = 'http://10.1.1.22:801/eportal/?c=ACSetting&a=Login&wlanuserip=&wlanacip=&wlanacname=&redirect=&session=&vlanid=0&port=&iTermType=1&protocol=http:'

        self.data = {'DDDDD': '311041210@telecom',
                     'upass': '041210',
                     'R1': '0',
                     'R2': '',
                     'R6': '0',
                     'para': '00',
                     '0MKKey': '123456'
                     }

        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'suffixType=@telecom; PHPSESSID=rre1coi1p0h6hs2oaua38cvb23',
            'Host': '10.1.1.22',
            'Referer': 'http://10.1.1.22/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }

    def requests_post(self):

        response = requests.post(self.url, self.data, headers=self.headers)

        if response.status_code == 200:
            print(f'响应代码:{response.status_code} 响应成功')
            if '您已经成功登录' in response.text:
                print('account: {}'.format(self.data['DDDDD']))
                print('password: {}'.format(self.data['upass']))
                print('登录成功')
            else:
                print('AC认证失败')
                print('网络测试中...')
                test_url = 'https://www.baidu.com/'
                print(f'测试网址: {test_url}')
                response_test = requests.get(test_url)
                if response_test.status_code == 200:
                    print(f'测试响应代码: {response_test.status_code} 连接成功')
                    print('网络已连接成功,请勿重复登陆')
                else:
                    print('测试失败,请重新尝试登陆')
        else:
            print('响应失败,请重新尝试(时间已过或网线wifi未连接)')

    def run(self):
        print(f'请求中,请求网址: {self.url}')
        self.requests_post()


if __name__ == '__main__':
    school = SchoolNetLogin()
    school.run()
    
