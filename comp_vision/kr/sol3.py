import pygame
import sys


WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
clock = pygame.time.Clock()

ANIM_STAY = pygame.image.load('animations/0.png')
ANIM_LEFT = [
    pygame.image.load('animations/l1.png'),
    pygame.image.load('animations/l2.png'),
    pygame.image.load('animations/l3.png'),
    pygame.image.load('animations/l4.png'),
    pygame.image.load('animations/l5.png')
]

ANIM_RIGHT = [
    pygame.image.load('animations/r1.png'),
    pygame.image.load('animations/r2.png'),
    pygame.image.load('animations/r3.png'),
    pygame.image.load('animations/r4.png'),
    pygame.image.load('animations/r5.png')
]

IMAGE_BACKGROUND = pygame.transform.smoothscale(pygame.image.load('animations/map.png'), (WIDTH, HEIGHT))

movement_type = "staying"
character_x = 10
character_y = HEIGHT * 0.73
current_frame = ANIM_STAY
frame_number = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and movement_type == "staying":
                movement_type = "right"
            elif event.key == pygame.K_a and movement_type == "staying":
                movement_type = "left"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and movement_type == "right":
                movement_type = "staying"
                current_frame = ANIM_STAY
                frame_number = 0
            if event.key == pygame.K_a and movement_type == "left":
                movement_type = "staying"
                current_frame = ANIM_STAY
                frame_number = 0

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_d] and movement_type == "staying":
        movement_type = "right"
    if pressed_keys[pygame.K_a] and movement_type == "staying":
        movement_type = "left"
    elif not(pressed_keys[pygame.K_a] or pressed_keys[pygame.K_d]):
        movement_type = "staying"

    if movement_type == "right":
        current_frame = ANIM_RIGHT[int(frame_number) % 5]
        frame_number += 0.2
        character_x += 2
    elif movement_type == "left":
        current_frame = ANIM_LEFT[int(frame_number) % 5]
        frame_number += 0.2
        character_x -= 2
    else:
        current_frame = ANIM_STAY
        frame_number = 0

    if character_x < 0:
        character_x = 0
    if character_x > WIDTH - 20:
        character_x = WIDTH - 20

    screen.blit(IMAGE_BACKGROUND, (0, 0))
    screen.blit(current_frame, (character_x, character_y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()