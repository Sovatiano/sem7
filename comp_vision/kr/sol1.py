import pygame
import sys


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
running = True


def draw_cells(size):
    horizontal_step = cells_size[0]
    vertical_step = cells_size[1]

    for y in range(vertical_step, HEIGHT, vertical_step):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (WIDTH, y))

    for x in range(horizontal_step, WIDTH, horizontal_step):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, HEIGHT))


def append_nums(cells_size):
    font = pygame.font.SysFont(None, int((WIDTH + HEIGHT) / 20))
    row_num = HEIGHT // cells_size[1]
    if cells_size[1] * row_num != HEIGHT:
        row_num += 1
    col_num = WIDTH // cells_size[0]
    if cells_size[0] * col_num != WIDTH:
        col_num += 1
    for row in range(row_num):
        for col in range(1, col_num + 1):
            cell_num = font.render(str(col + row * col_num), True, (0, 0, 0))
            screen.blit(cell_num, (col * cells_size[0] - cells_size[0] * 0.75,
                                   row * cells_size[1] + cells_size[1] * 0.25))


pygame.init()
cells_size = [135, 100]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30, 144, 255))

    draw_cells(cells_size)
    append_nums(cells_size)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()