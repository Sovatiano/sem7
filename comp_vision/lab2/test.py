import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Машинка")

SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
GRAY = (80, 80, 80)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
YELLOW = (255, 255, 0)

car_x = WIDTH // 2 - 40
car_y = HEIGHT - 180
car_width = 80
car_height = 40
car_speed = 5

road_y = HEIGHT - 120
road_height = 120

button_width = 100
button_height = 50
forward_button = pygame.Rect(WIDTH - 120, 20, button_width, button_height)
backward_button = pygame.Rect(20, 20, button_width, button_height)

forward_pressed = False
backward_pressed = False

clouds = [
    [100, 80, 120, 40],
    [400, 120, 150, 50],
    [600, 60, 100, 35],
    [200, 150, 130, 45]
]

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if forward_button.collidepoint(mouse_pos):
                forward_pressed = True
            if backward_button.collidepoint(mouse_pos):
                backward_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            forward_pressed = False
            backward_pressed = False

    if forward_pressed:
        car_x += car_speed
    if backward_pressed:
        car_x -= car_speed

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    if car_x < 0:
        car_x = 0
    if car_x > WIDTH - car_width:
        car_x = WIDTH - car_width

    screen.fill(SKY_BLUE)

    for cloud in clouds:
        pygame.draw.ellipse(screen, WHITE, (cloud[0], cloud[1], cloud[2], cloud[3]))
        pygame.draw.ellipse(screen, WHITE, (cloud[0] + 20, cloud[1] - 15, cloud[2] - 40, cloud[3]))
        pygame.draw.ellipse(screen, WHITE, (cloud[0] + 40, cloud[1], cloud[2] - 40, cloud[3]))

    pygame.draw.rect(screen, GRAY, (0, road_y, WIDTH, road_height))

    for i in range(0, WIDTH, 60):
        pygame.draw.rect(screen, YELLOW, (i, road_y + road_height // 2 - 2, 30, 4))

    car_body = pygame.Rect(car_x, car_y, car_width, car_height)
    pygame.draw.rect(screen, RED, car_body)

    car_top = pygame.Rect(car_x + 10, car_y - 25, car_width - 30, 25)
    pygame.draw.rect(screen, RED, car_top)

    window = pygame.Rect(car_x + 50, car_y - 20, 20, 15)
    pygame.draw.rect(screen, BLUE, window)

    wheel1 = pygame.Rect(car_x + 5, car_y + car_height - 10, 15, 20)
    wheel2 = pygame.Rect(car_x + car_width - 20, car_y + car_height - 10, 15, 20)
    pygame.draw.ellipse(screen, BLACK, wheel1)
    pygame.draw.ellipse(screen, BLACK, wheel2)

    headlight = pygame.Rect(car_x + car_width - 10, car_y + 5, 8, 8)
    pygame.draw.ellipse(screen, YELLOW, headlight)

    forward_color = DARK_GREEN if forward_pressed else GREEN
    backward_color = DARK_GREEN if backward_pressed else GREEN

    pygame.draw.rect(screen, forward_color, forward_button)
    pygame.draw.rect(screen, backward_color, backward_button)

    font = pygame.font.SysFont(None, 30)
    forward_text = font.render("Вперёд", True, BLACK)
    backward_text = font.render("Назад", True, BLACK)

    screen.blit(forward_text, (forward_button.x + 20, forward_button.y + 15))
    screen.blit(backward_text, (backward_button.x + 25, backward_button.y + 15))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()