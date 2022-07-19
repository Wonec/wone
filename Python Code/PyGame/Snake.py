from pygame.locals import *
import pygame
import random
import time
import sys


class Snake:

    def __init__(self):
        # 设置窗口标题
        pygame.display.set_caption('Snake')

        # 设置窗口图标
        image = pygame.image.load("img/kela.ico")
        pygame.display.set_icon(image)

        # 帧率
        self.FPS = pygame.time.Clock()
        # 界面尺寸
        self.Surface = pygame.display.set_mode((640, 480))

        # 颜色设置
        self.red = (255, 0, 0)
        self.grey = (150, 150, 150)
        self.snow = (205, 205, 201)
        self.white = (255, 255, 255)
        self.orange = (250, 100, 85)

        # 蛇与果实初始设置
        self.snake_position = [100, 100]  # 蛇初始位置
        self.snake_length = [[100, 100], [80, 100], [60, 100]]  # 蛇的身体 初始为3个
        self.fruit_position = [300, 300]  # 果实初始位置
        self.fruit_status = 1  # 果实状态: 1 代表没吃掉 0 代表被吃
        self.direction = 'down'  # 蛇初始运动方向
        self.direction_change = self.direction  # 蛇运动方向
        self.score = 0  # 分数
        self.game = 0  # 游戏状态

    # 显示文字
    def Font(self, size, message, position, color):
        Font = pygame.font.Font('img/baddf.ttf', size)
        Surf = Font.render(message, True, color)
        Rect = Surf.get_rect()
        Rect.midtop = position
        self.Surface.blit(Surf, Rect)

    # 游戏结束显示文字
    def game_over_show_text(self):
        # 显示游戏结束字体及大小
        self.Font(60, "Game Over", (320, 125), self.red)
        # 显示分数字体及大小
        self.Font(35, "SCORE: " + str(self.score), (320, 195), self.red)
        # 重新开始游戏
        self.Font(25, "Will restart the game, Press 'esc' end the game", (320, 245), self.red)
        # 刷新界面显示
        pygame.display.update()
        self.game = 0

    # 键盘控制
    def control(self):
        # 获取事件
        for event in pygame.event.get():
            # 执行关闭按钮退出
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # 执行键盘事件
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    self.direction_change = 'right'
                if event.key == K_LEFT or event.key == K_a:
                    self.direction_change = 'left'
                if event.key == K_UP or event.key == K_w:
                    self.direction_change = 'up'
                if event.key == K_DOWN or event.key == K_s:
                    self.direction_change = 'down'
                if event.key == K_ESCAPE:  # ESC结束游戏
                    pygame.event.post(pygame.event.Event(QUIT))

    # 果实被吃重新生成果实
    def new_fruit(self):
        self.score += 1
        x = random.randrange(1, 32)
        y = random.randrange(1, 24)
        # 判断刷新位置是否与身体重合
        for s in self.snake_length:
            while x * 20 == s[0] and y * 20 == s[1]:
                x = random.randrange(1, 32)
                y = random.randrange(1, 24)
            else:
                self.fruit_position = [int(x * 20), int(y * 20)]
                self.fruit_status = 1

    # 绘制蛇与果实 显示分数长度
    def draw(self):
        # 绘制游戏显示层
        self.Surface.fill(self.white)

        # 网格
        for x in range(0, 660, 20):
            pygame.draw.line(self.Surface, (0, 0, 0), (x, 0), (x, 480), 1)
        for y in range(0, 500, 20):
            pygame.draw.line(self.Surface, (0, 0, 0), (0, y), (640, y), 1)

        # 蛇身
        for position in self.snake_length[1:]:
            pygame.draw.rect(self.Surface, self.snow, Rect(position[0], position[1], 20, 20))
        # 蛇头
        pygame.draw.rect(self.Surface, self.grey, Rect(self.snake_position[0], self.snake_position[1], 20, 20))
        # 果实
        pygame.draw.rect(self.Surface, self.red, Rect(self.fruit_position[0], self.fruit_position[1], 20, 20))

        # 分数显示
        self.Font(28, "SCORE: " + str(self.score), (80, 10), self.orange)
        # 长度显示
        self.Font(28, "LENGTH: " + str(len(self.snake_length)), (86, 40), self.orange)

    # 游戏运行
    def run(self):
        # 初始化
        pygame.init()
        # 开始游戏主循环
        while True:
            # 键盘控制方法
            self.control()

            # 判断是否运动方向是否为当前方向的反方向
            if self.direction_change == 'right' and not self.direction == 'left':
                self.direction = self.direction_change
            if self.direction_change == 'left' and not self.direction == 'right':
                self.direction = self.direction_change
            if self.direction_change == 'up' and not self.direction == 'down':
                self.direction = self.direction_change
            if self.direction_change == 'down' and not self.direction == 'up':
                self.direction = self.direction_change

            # 根据键盘控制方向更改蛇头坐标
            if self.direction == 'right':
                self.snake_position[0] += 20
            if self.direction == 'left':
                self.snake_position[0] -= 20
            if self.direction == 'up':
                self.snake_position[1] -= 20
            if self.direction == 'down':
                self.snake_position[1] += 20

            # 更改的坐标重新插入蛇身体
            self.snake_length.insert(0, list(self.snake_position))

            # 判断蛇是否吃到果实 没吃到则去除尾部
            if self.snake_position[0] == self.fruit_position[0] and self.snake_position[1] == self.fruit_position[1]:
                self.fruit_status = 0
            else:
                self.snake_length.pop()

            # 果实被吃后重新生成
            if self.fruit_status == 0:
                self.new_fruit()

            # 绘制蛇果实界面方法
            self.draw()

            # 刷新界面
            pygame.display.update()

            # 判断蛇是否触碰到游戏边界
            if self.snake_position[0] >= 640 or self.snake_position[0] < 0:
                self.game = 1
            if self.snake_position[1] >= 480 or self.snake_position[1] < 0:
                self.game = 1

            # 判断蛇是否碰到自己身体
            for snakeBody in self.snake_length[1:]:
                if self.snake_position[0] == snakeBody[0] and self.snake_position[1] == snakeBody[1]:
                    self.game = 1

            # 判断游戏状态 重新开始游戏
            if self.game == 1:
                self.game_over_show_text()
                time.sleep(4)
                # 重新初始化设置
                self.__init__()
                self.run()

            # 增加游戏难度 通过长度增加速度
            if len(self.snake_length) < 40:
                speed = 10 + len(self.snake_length) // 10
            else:
                speed = 14 + len(self.snake_length) // 20

            # 设置帧率
            self.FPS.tick(speed)


if __name__ == '__main__':
    snake = Snake()
    snake.run()
