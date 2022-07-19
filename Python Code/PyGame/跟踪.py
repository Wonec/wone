import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("test")
clock = pygame.time.Clock()
target = pygame.Rect(200, 200, 10, 10)
tracer = pygame.Rect(0, 0, 10, 10)
speed = 5


def trace(target, tracer):
    # 应为pygame的rect函数只接受int类型数，所以为了不影响计算精度，我们先暂时定义两个数用于计算，最后将这连个数传入rect即可
    x1, y1 = tracer.x, tracer.y
    x2, y2 = target.x, target.y  # 同上
    dx = x2 - x1
    dy = y1 - y2
    r = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
    try:
        sin = dy / r
        cos = dx / r
        tracer.x += cos * speed
        tracer.y -= sin * speed
    except:
        pass
    # tracer.x, tracer.y = x1, y1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(60)
    screen.fill((255, 255, 255))
    # ************填写内容*********************
    mouse_pos = pygame.mouse.get_pos()
    target.x, target.y = (mouse_pos)
    pygame.draw.rect(screen, (255, 0, 0), target)
    pygame.draw.rect(screen, (0, 255, 0), tracer)
    trace(target, tracer)
    # ***************************************

    pygame.display.update()
