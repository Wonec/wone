# 导入模块
from random import randint
import time

print('    ----------------------------------')
print('                 《规则》')
print('                  下注')
print('            扔出7、11点玩家胜利')
print('           扔出2、3、12点庄家胜利')
print('          若扔出的点数不在以上范围')
print('             则开始下一轮扔点')
print('      玩家扔出点数若与第一轮扔出点数相同')
print('               那么玩家胜利')
print('              若扔出点数为 7')
print('               那么庄家胜利')
print('    ---------------------------------')

# 开始游戏循环
while True:

    # 读取文件
    with open('资产.txt', 'r+') as f:
        a = f.read()

        if len(a) == 0:
            f.write('1000')
            f.close()
            f = open('资产.txt', 'r')
            a = f.read()
            money = int(a)
        else:
            money = int(a)

        if money <= 0:
            a = input(f'您的资产为{money}\n是否加上1000块(yes/no)').replace(' ','')
            if a == 'yes':
                f.write('1000')
                f.close()
                f = open('资产.txt', 'r')
                a = f.read()
                money = int(a)
                print('已为您加上1000元')
            elif a == 'no':
                break
            else:
                print('输入有误,请重新输入')

        else:
            print('\n你的总资产为%d元' % money)
            go_on = False  # 设置下一轮开关
            # 下注
            while True:
                # 测试
                try:
                    bet = int(input('请下注:'))
                    if 0 < bet <= money:
                        break
                    elif bet <= 0:
                        print('赌注不可为负数')
                    else:
                        print('超出你所拥有的资产')

                except ValueError:
                    print('请输入整数')

            # 扔骰子
            first = randint(1, 6) + randint(1, 6)
            print('你扔出了%d点' % first)
            time.sleep(0.5)

            # 判断
            if first == 7 or first == 11:
                with open('资产.txt', 'w') as f:
                    f.write(str(money + bet))
                    f.close()
                print('玩家胜')
            elif first == 2 or first == 3 or first == 12:
                with open('资产.txt', 'w') as f:
                    f.write(str(money - bet))
                    f.close()
                print('庄家胜')
            else:
                go_on = True
                time.sleep(0.5)

                # 下一轮
                while go_on:
                    print('游戏继续')
                    go_on = False
                    second = randint(1, 6) + randint(1, 6)
                    print('你扔出了%d点' % second)
                    time.sleep(0.5)

                    # 判断点数
                    if second == 7:
                        with open('资产.txt', 'w') as f:
                            f.write(str(money - bet))
                            f.close()
                        print('庄家胜')
                    elif second == first:
                        with open('资产.txt', 'w') as f:
                            f.write(str(money + bet))
                            f.close()
                        print('玩家胜')
                    else:
                        go_on = True
                        time.sleep(0.5)

print('----你破产了,游戏结束----')
print('----十赌九输,不赌为上----')
input('回车退出:')
