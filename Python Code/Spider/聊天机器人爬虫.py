import requests
import json


class ChatBot(object):
    """聊天机器人的类"""

    # 1.初始化属性
    def __init__(self):
        self.url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
        print('机器人:您好！这里是大聪明，非常欢迎您的到来，有什么想和我聊聊的吗？')

    # 2.请求网址
    def get_response(self):
        response = requests.get(url=self.new_url).text
        return response

    # 3.解析提取数据
    def extract_response(self):
        data = json.loads(self.get_response())
        text = data['content'].replace('菲菲', '大聪明').replace('{br}', '\n')
        print(f'机器人:{text}')

    # 4.调用方法
    def main(self):
        while True:
            self.msg = input('我 :')
            if self.msg == 'q':
                print('\n-------已退出-------')
                break
            else:
                self.new_url = self.url + self.msg
                self.get_response()
                self.extract_response()


if __name__ == '__main__':
    chatbot = ChatBot()  # 实例化对象
    chatbot.main()  # 调用main()函数
