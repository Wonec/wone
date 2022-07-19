import random
import pygame
from pygame.locals import *

# 设置宽高
width, height = (1000, 800)

# 设置界面 标题
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Typing Game')
# 设置图标
image = pygame.image.load('img/kela.ico')
pygame.display.set_icon(image)

# 定义颜色
white = (225, 225, 225)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (220, 80, 25)

# 字母移动时间 刷新时间
diff_ticks = 20
ticks = pygame.time.get_ticks() + diff_ticks
word_diff_ticks = 1000
word_ticks = pygame.time.get_ticks() + word_diff_ticks


# 生成字母方法
def get_random_word():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x = random.randint(100, height - 100)
    y = 0
    word = random.randint(65, 90)  # ASCII编码表 A-Z
    return x, y, word, color


# 存放字母的列表
word_list = []

# 清除字母的个数
clear_word = 0
# 难度等级
level = 1
# 游戏状态 是否闪烁
game_state = True
flash = True

while True:
    # 初始化
    pygame.init()
    # 设置字体
    my_font = pygame.font.Font('img/baddf.ttf', 55)
    # 获取事件
    for event in pygame.event.get():
        # 退出
        if event.type == QUIT:
            pygame.quit()
            exit()
        # 键盘控制
        elif event.type == KEYDOWN:
            if game_state == True and len(word_list) > 0:
                if event.key == word_list[0][2] + 32:  # ASCII 编码大小写字母差32位
                    word_list.pop(0)
                    clear_word += 1
                if event.key == K_ESCAPE:  # ESC结束游戏
                    pygame.event.post(pygame.event.Event(QUIT))

                # 关卡 难度提升设置
                if clear_word >= level * 10:
                    level += 1
                    diff_ticks = diff_ticks * 0.85
                    word_diff_ticks = word_diff_ticks * 0.9
    # 背景填充
    screen.fill(white)

    # 显示难度等级到屏幕
    font_level = my_font.render(f'Level: {level}', True, orange)
    w, h = font_level.get_size()
    screen.blit(font_level, (0, 800 - h))

    # 绘制字母
    for i in range(len(word_list)):
        x, y, word, color = word_list[i]
        # 首字母闪烁
        if i == 0 and flash:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        textImage = my_font.render(chr(word), True, color)
        screen.blit(textImage, (x, y))

    # 游戏结束
    if game_state == False:
        screen.fill(black)  # 填充背景为黑色
        # 显示文字
        game_over_text = my_font.render("Level %d Fail" % level, True, red)
        cw, ch = game_over_text.get_size()
        screen.blit(game_over_text, ((width - cw) / 2, (height - ch) / 2))  # 居中显示

    # 游戏进行中
    if game_state == True:
        # 字母刷新条件
        if pygame.time.get_ticks() >= word_ticks:
            word_ticks += word_diff_ticks
            word_list.append(get_random_word())
        # 字母移动条件
        if pygame.time.get_ticks() >= ticks:
            ticks += diff_ticks
            flash = not flash  # 移动一次一闪
            # 字母移动
            for i in range(len(word_list)):
                x, y, word, color = word_list[i]
                word_list[i] = (x, y + 1, word, color)  # 每次移动 1 像素

            # 游戏结束条件(当字母碰到底部)
            if len(word_list) > 0 and word_list[0][1] > height - h + 5:
                game_state = False
    # 更新显示
    pygame.display.update()
