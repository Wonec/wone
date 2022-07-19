import requests
import time


class Image(object):
    def __init__(self):
        self.url = 'https://image.baidu.com/search/acjson?'
        self.headers = {
            'Cookie': 'BDqhfp=gou%26%26NaN-1undefined%26%260%26%261; BIDUPSID=8AD1D0DFA4DD46891FB498C431BC9A5F; PSTM=1614517517; BAIDUID=8AD1D0DFA4DD46890D552D6E582EE574:FG=1; __yjs_duid=1_1a35c7ccb116e7a3dabcd2e1160657461617367128145; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=33810_33815_33746_33273_33691_33757_26350; firstShowTip=1; BAIDUID_BFESS=8AD1D0DFA4DD46890D552D6E582EE574:FG=1; delPer=0; PSINO=6; ZD_ENTRY=empty; indexPageSugList=%5B%22%E7%8B%97%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=null; ab_sr=1.0.0_NWFiNzQ1YTdmMzlmNDIzZTE2ZDQzYmRhYjA1ODVjMTZlNDY5MTdjZDE1OGJiMDMzOTRjMzA4MGUyMjgzNGQ4OTQ0ZmU5ZDVhZjI0ZjdhNGRlNjlmMDJiOWUwMDc0Nzdj; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }
        self.params = {
            'tn': 'resultjson_com',
            'logid': '11082984189123110440',
            'ipn': 'rj',
            'fp': 'result',
            'word': '',
            'pn': '',
            'rn': '30',
            'time': ''
        }
        self.image_list = []
        self.image_name = []

    def get_image(self):
        self.params['word'] = input('请输入你想要获取的图片:')
        # self.params['queryWord'] = self.params['word']
        num = int(input('请输入想要获取图片的页数(每页有30张图片):'))
        for i in range(0, num):
            self.params['time'] = int(time.time() * 1000)
            self.params['pn'] = i * 30
            response = requests.get(url=self.url, headers=self.headers, params=self.params)
            for j in range(0, len(response.json()['data']) - 1):
                self.image_list.append(response.json()['data'][j]['thumbURL'])
                self.image_name.append(response.json()['data'][j]['fromPageTitleEnc'])

    def save_image(self):
        num = 0
        for i in self.image_list:
            image = requests.get(url=i)
            title = self.image_name[num].replace('?', '').replace('*', '').replace('"', '').replace('\\', '').replace(
                '/', '').replace(':', '').replace('<', '').replace('>', '').replace('|', '')
            num += 1
            with open('百度图片/{}.jpg'.format(title), 'wb') as f:
                f.write(image.content)
            print(f'正在获取:{title}')


if __name__ == '__main__':
    image = Image()
    image.get_image()
    image.save_image()
