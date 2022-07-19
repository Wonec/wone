import sys
import pygame
from pygame.locals import *

pygame.init()

# 参数设置
space = 60
cell_size = 40
cell_num = 15
grid_size = cell_size * (cell_num - 1) + space * 2

# 窗口设置
pygame.display.set_caption("GoBang")
image = pygame.image.load('img/kela.ico')
pygame.display.set_icon(image)
screen = pygame.display.set_mode((grid_size, grid_size))

# 存储棋子
chess_arr = []
flag = 1  # 1 黑 2 白
game_state = 1  # 1 表示游戏正常运行
step = 0
go_back = 3


def get_one_dire_num(lx, ly, dx, dy, m):
    tx = lx
    ty = ly
    s = 0
    while True:
        tx += dx
        ty += dy
        if tx < 0 or tx >= cell_num or ty < 0 or ty >= cell_num or m[ty][tx] == 0:
            return s
        s += 1


def check_win(chess_arr, flag):
    m = [[0] * cell_num for i in range(cell_num)]  # 定义一个15 x 15 数组
    for x, y, c in chess_arr:
        if c == flag:
            m[y][x] = 1  # 有棋则标1
    lx = chess_arr[-1][0]
    ly = chess_arr[-1][1]
    dire_arr = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]

    for dire1, dire2 in dire_arr:
        dx, dy = dire1
        num1 = get_one_dire_num(lx, ly, dx, dy, m)
        dx, dy = dire2
        num2 = get_one_dire_num(lx, ly, dx, dy, m)
        if num1 + num2 + 1 >= 5:
            return True

    return False


# 游戏主循环
while True:
    # 检查事件
    for event in pygame.event.get():  # 点击退出
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if game_state == 1 and event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            xi = int(round((x - space) * 1.0 / cell_size))
            yi = int(round((y - space) * 1.0 / cell_size))
            if xi >= 0 and xi < cell_num and yi >= 0 and yi < cell_num and (xi, yi, 1) not in chess_arr and (
                    xi, yi, 2) not in chess_arr:
                chess_arr.append((xi, yi, flag))
                step += 1
                if check_win(chess_arr, flag):
                    game_state = 2 if flag == 1 else 3
                else:
                    flag = 2 if flag == 1 else 1

        if event.type == KEYDOWN:
            if len(chess_arr) > 0 and event.key == K_b and go_back > 0 and game_state == 1:
                chess_arr.pop()
                step -= 1
                go_back -= 1

    # 背景填充x
    screen.fill((250, 120, 45))

    # 绘制棋盘
    for x in range(0, cell_size * cell_num, cell_size):
        pygame.draw.line(screen, (0, 0, 0), (x + space, 0 + space),
                         (x + space, cell_size * (cell_num - 1) + space), 1)
    for y in range(0, cell_size * cell_num, cell_size):
        pygame.draw.line(screen, (0, 0, 0), (0 + space, y + space),
                         (cell_size * (cell_num - 1) + space, y + space), 1)

    # 绘制棋子
    for x, y, f in chess_arr:
        chess_color = (30, 30, 30) if f == 1 else (215, 215, 215)
        pygame.draw.circle(screen, chess_color, [x * cell_size + space, y * cell_size + space], 15, 15)

    my_font = pygame.font.Font('img/baddf.ttf', 33)
    color = 0, 0, 0
    now_text = "Now is "
    # now_text = "Now is %s" % ('black' if flag == 1 else 'white')
    textImage = my_font.render(now_text, True, color)
    screen.blit(textImage, (55, 10))

    pygame.draw.circle(screen, (0, 0, 0) if flag == 1 else (255, 255, 255), [190, 28], 15, 15)

    my_font = pygame.font.Font('img/baddf.ttf', 33)
    color = 0, 0, 0
    step_text = "Step: %d" % step
    textImage = my_font.render(step_text, True, color)
    screen.blit(textImage, (grid_size / 2 + 110, 10))

    my_font = pygame.font.Font('img/baddf.ttf', 30)
    color = 0, 0, 0
    back_text = "Enter 'B' go back Previous             Step : %d" % go_back
    textImage = my_font.render(back_text, True, color)
    screen.blit(textImage, (10, grid_size - 40))

    if game_state != 1:
        my_font = pygame.font.Font('img/baddf.ttf', 50)
        white = 255, 255, 255
        win_text = "%s win" % ('black' if game_state == 2 else 'white')
        textImage = my_font.render(win_text, True, (255, 255, 255) if game_state == 3 else (0, 0, 0))
        screen.blit(textImage, (225, grid_size / 2 - 50))

    # 显示更新
    pygame.display.update()
