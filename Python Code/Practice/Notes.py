import datetime
import os
import csv
import re
import sys


class Jilu:

    def __init__(self):
        self.os()
        os.system('color c')
        print('''
        ---------------
        | 时间管理大师|
        |1.新建记录   |
        |2.查看记录   |
        |3.删除数据   |
        |4.分析数据   |
        |5.更改数据   |
        |(q退出程序)  |
        |             |
        ---------------''')
        self.f = open(
            '/Users/wone/Desktop/PythonCode/Practice/Notes.csv', 'r+')
        self.csv = csv.writer(self.f)

    def os(self):
        os.system('cls')

    def csv_1(self, num, datetime, category, text, time):
        with open('/Users/wone/Desktop/PythonCode/Practice/Notes.csv', 'a+', newline='') as f:
            a = csv.writer(f)
            a.writerow([num, datetime, category, text, time])
            f.close()

    def res_1(self):
        while True:
            self.res = input('输入b返回主界面\nq退出程序:')
            if self.res == 'b':
                self.__init__()
                break
            elif self.res == 'q':
                sys.exit()
            else:
                print('输入错误')

    def jilu(self):
        self.os()
        print('----新建记录----')
        with open('/Users/wone/Desktop/PythonCode/Practice/Notes.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                num = int(row[0]) + 1
        now = f'{datetime.datetime.now().year}年{datetime.datetime.now().month}月{datetime.datetime.now().day}日'
        sj = input('请输入时间(xx时xx分,天默认为今天):')
        dt = f'{now}{sj}'
        while True:
            ca = input('请输入分类(运动,学习,游戏,其他):')
            if ca in ['运动', '学习', '游戏', '其他']:
                break
            else:
                print('没有这个分类请重新输入')
        tt = input('请输入具体做了什么:')
        tm = input('请输入多长时间:')
        self.csv_1(num, dt, ca, tt, tm)
        self.res_1()

    def chakan(self, text='查看'):
        self.os()
        print(f'                ----{text}记录----\n')
        with open('Notes.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                for r in row:
                    print(r, end=' | ')
                print('\n')

    def fenxi(self):
        self.os()
        print('----分析数据----')
        with open('Notes.csv', 'r') as f:
            reader = csv.reader(f)
            yd = 0
            xx = 0
            yx = 0
            qt = 0
            h = 0
            m = 0
            for row in reader:
                if row[2] == '运动':
                    yd += 1
                elif row[2] == '学习':
                    xx += 1
                elif row[2] == '游戏':
                    yx += 1
                elif row[2] == '其他':
                    qt += 1
                if '小时' in row[4] and '分钟' in row[4]:
                    h1 = re.findall('(\d+)小时', row[4])
                    for i in h1:
                        h += int(i)
                    m1 = re.findall('(\d+)分钟', row[4])
                    for b in m1:
                        m += int(b)
                        if m >= 60:
                            m -= 60
                            h += 1
                elif '小时' in row[4]:
                    h += int(row[4].replace('小时', ''))
                elif '分钟' in row[4]:
                    m += int(row[4].replace('分钟', ''))
                    if m >= 60:
                        m -= 60
                        h += 1
            print(f'\n运动{yd}次 | 学习{xx}次 \n\n游戏{yx}次 | 其他{qt}次 \n')
            all = yd + xx + yx + qt
            yd_b = float(yd/all) * 100
            xx_b = float(xx/all) * 100
            yx_b = float(yx/all) * 100
            qt_b = float(qt/all) * 100
            print('运动占比{:.2f}% | 学习占比{:.2f}% \n\n游戏占比{:.2f}% | 其他占比{:.2f}%\n'.format(
                yd_b, xx_b, yx_b, qt_b))
            print(f'共用{h}小时{m}分钟\n')
        self.res_1()

    def remove(self):
        self.chakan(text='删除')
        with open('Notes.csv', 'r', newline='') as inp:
            data = csv.reader(inp)
            newrows = []
            while True:
                for row in data:
                    newrows.append(row)
                num = input("输入想要删除的行(输入q取消):")
                if num == 'q':
                    break
                elif num not in [c[0] for c in newrows]:
                    print('不在行数范围')
                else:
                    for e in newrows[int(num)]:
                        print(e, end=" | ")
                    while True:
                        r = input('\n是否删除(是/否):')
                        if r == '是':
                            with open('Notes.csv', 'w', newline='') as out:
                                csv_writer = csv.writer(out)
                                n = 0
                                for a in newrows:
                                    if a[0] != num:
                                        a[0] = n
                                        csv_writer.writerow(a)
                                        n += 1
                            print('删除成功')
                            break
                        elif r == '否':
                            break
                        else:
                            print('输入错误')
                    break
            self.res_1()

    def xiugai(self):
        self.chakan(text='更改')
        with open('Notes.csv', 'r', newline='') as inp:
            data = csv.reader(inp)
            newrows = []
            while True:
                for row in data:
                    newrows.append(row)
                num = input("输入想要更改的行(输入q取消):")
                if num == 'q':
                    break
                elif num not in row[0]:
                    print('超出行数范围')
                else:
                    with open('Notes.csv', 'w', newline='') as out:
                        csv_writer = csv.writer(out)
                        for a in newrows:
                            if a[0] != num:
                                csv_writer.writerow(a)
                            elif a[0] == num:
                                now = f'{datetime.datetime.now().year}年{datetime.datetime.now().month}月{datetime.datetime.now().day}日'
                                sj = input('请输入时间(xx时xx分,天默认为今天):')
                                dt = f'{now}{sj}'
                                while True:
                                    ca = input('请输入分类(运动,学习,游戏,其他):')
                                    if ca in ['运动', '学习', '游戏', '其他']:
                                        break
                                    else:
                                        print('没有这个分类请重新输入')
                                tt = input('请输入具体做了什么:')
                                tm = input('请输入多长时间:')
                                print(f'修改内容:{dt} | {ca} | {tt} | {tm}')
                                while True:
                                    e = input('是否修改(是/否)')
                                    if e == '是':
                                        csv_writer.writerow(
                                            [a[0], dt, ca, tt, tm])
                                        print('修改成功')
                                        break
                                    elif e == '否':
                                        break
                                    else:
                                        print('输入错误')
                break
            self.res_1()

    def run(self):
        text = self.f.readlines()
        if not text:
            self.csv_1('0', '日期', '类别', '内容', '时间')
            self.f.close()
        while True:
            back = input('请输入:')

            if back == '1':
                self.jilu()
            elif back == '2':
                self.chakan()
                self.res_1()
            elif back == '3':
                self.remove()
            elif back == '4':
                self.fenxi()
            elif back == '5':
                self.xiugai()
            elif back == 'q':
                sys.exit()
            else:
                print('输入错误')


if __name__ == '__main__':
    jl = Jilu()
    jl.run()
