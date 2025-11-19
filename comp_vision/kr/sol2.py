import time
import random
import pygame
import sys

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


running = True
square_x = 350
square_y = 250
movement_type = "right"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("w")
            elif event.key == pygame.K_d:
                print("d")
            elif event.key == pygame.K_s:
                print("s")
            elif event.key == pygame.K_a:
                print("a")
            elif event.key == pygame.K_RETURN:
                print("enter")
            elif event.key == pygame.K_SPACE:
                print("space")
            elif event.key == pygame.K_ESCAPE:
                print("escape")

    color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    pygame.draw.rect(screen, color, (square_x, square_y, 10, 10))
    if movement_type == "right":
        square_x += 10
        if square_x == 440:
            movement_type = "down"
    elif movement_type == "down":
        square_y += 10
        if square_y == 340:
            movement_type = "left"
    elif movement_type == "left":
        square_x -= 10
        if square_x == 350:
            movement_type = "up"
    else:
        square_y -= 10
        if square_y == 250:
            movement_type = "right"
            pygame.draw.rect(screen, color, (square_x, square_y, 10, 10))
            pygame.display.flip()
            time.sleep(0.1)
            screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
sys.exit()