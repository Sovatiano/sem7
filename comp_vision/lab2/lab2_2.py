import pygame
import sys
import math as m
from Car import Car

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Савостьянов. АА-22-07")

WHITE = (255, 255, 255)
DARK_RED = (100, 0, 0)
GRAY = (100, 100, 100)
BLUE = (30, 144, 255)
YELLOW = (255, 255, 0)
BUTTON_COLOR = (0, 180, 0)
BUTTON_TEXT_COLOR = (0, 0, 0)
CLOUDS = [
    [100, 80, 120, 40],
    [400, 120, 150, 50],
    [600, 60, 100, 35],
    [200, 150, 130, 45]
]
ROAD_Y = HEIGHT * 0.75
ROAD_HEIGHT = HEIGHT * 0.25

BUTTON_WIDTH = WIDTH * 0.17
BUTTON_HEIGHT = HEIGHT * 0.05

forward_button = pygame.Rect(WIDTH * 0.75, HEIGHT * 0.4, BUTTON_WIDTH, BUTTON_HEIGHT)
backward_button = pygame.Rect(WIDTH * 0.1, HEIGHT * 0.4, BUTTON_WIDTH, BUTTON_HEIGHT)
draw_car_button = pygame.Rect(WIDTH * 0.75, HEIGHT * 0.9, BUTTON_WIDTH, BUTTON_HEIGHT)
forward_pressed = False
backward_pressed = False
draw_pressed = False



def draw_clouds():
    for cloud in CLOUDS:
        pygame.draw.ellipse(screen, WHITE, (cloud[0], cloud[1], cloud[2], cloud[3]))
        pygame.draw.ellipse(screen, WHITE, (cloud[0] + 20, cloud[1] - 15, cloud[2] - 40, cloud[3]))
        pygame.draw.ellipse(screen, WHITE, (cloud[0] + 40, cloud[1], cloud[2] - 40, cloud[3]))


def draw_road():
    pygame.draw.rect(screen, GRAY, (0, ROAD_Y, WIDTH, ROAD_HEIGHT))
    for i in range(0, WIDTH, 60):
        pygame.draw.rect(screen, YELLOW, (i, ROAD_Y + ROAD_HEIGHT // 2 - 2, 30, 4))

def draw_buttons():
    font = pygame.font.SysFont(None, int((WIDTH + HEIGHT) / 50))
    forward_text = font.render("Вперёд", True, BUTTON_TEXT_COLOR)
    backward_text = font.render("Назад", True, BUTTON_TEXT_COLOR)
    draw_text = font.render("Нарисовать", True, BUTTON_TEXT_COLOR)

    pygame.draw.rect(screen, BUTTON_COLOR, draw_car_button)
    # pygame.draw.rect(screen, BUTTON_COLOR, forward_button)
    # pygame.draw.rect(screen, BUTTON_COLOR, backward_button)

    # screen.blit(forward_text, (forward_button.x + forward_button.width * 0.2,forward_button.y + forward_button.height * 0.15))
    # screen.blit(backward_text, (backward_button.x + backward_button.width * 0.25,backward_button.y + backward_button.height * 0.15))
    screen.blit(draw_text, (draw_car_button.x + draw_car_button.width * 0.1, draw_car_button.y + draw_car_button.height * 0.15))


car = Car(100, 430, DARK_RED, WIDTH, screen)
moving_trajectory = 'right'

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # if forward_button.collidepoint(mouse_pos):
            #     forward_pressed = True
            # if backward_button.collidepoint(mouse_pos):
            #     backward_pressed = True
            if draw_car_button.collidepoint(mouse_pos):
                car = Car(100, 430, DARK_RED, WIDTH, screen)
                moving_trajectory = 'right'
                draw_pressed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            forward_pressed = False
            backward_pressed = False

    if forward_pressed:
        car.move_right()
    if backward_pressed:
        car.move_left()


    if car.x == WIDTH - car.width * 1.05:
        moving_trajectory = 'left'
        car.flip()
    if car.x == car.width * 0.05:
        moving_trajectory = 'right'
        car.flip()

    if moving_trajectory == 'right':
        car.move_right()
    else:
        car.move_left()

    screen.fill(BLUE)
    draw_clouds()
    draw_road()
    draw_buttons()

    if draw_pressed:
        car.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
