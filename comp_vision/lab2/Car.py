import pygame.draw


class Car:
    def __init__(self, x, y, main_color, screen_width, surface):
        self.x = x
        self.y = y
        self.main_color = main_color
        self.screen_width = screen_width
        self.main_surface = surface
        self.width = 150
        self.height = 50
        self.surface = pygame.Surface((self.width, self.height * 1.3), pygame.SRCALPHA)
        self.sub_surface = pygame.Surface((self.width * 1.1, self.height * 1.3), pygame.SRCALPHA)
        self.speed = 5
        self.direction = 1
        self.COLORS = {
            "CAR_COLOR": main_color,
            "WHEEL_COLOR": (0, 0, 0),
            "WINDOWS_COLOR": (20, 104, 255),
            "DETAILS_COLOR": (45, 45, 45),
            "FRONT_LIGHT_COLOR": (255, 255, 155),
            "BACK_LIGHT_COLOR": (255, 50, 50)
        }

    def move_right(self):
        self.x += self.speed
        if self.x > self.screen_width - self.width * 1.05:
            self.x = self.screen_width - self.width * 1.05

    def move_left(self):
        self.x -= self.speed
        if self.x - self.width * 0.05 < 0:
            self.x = self.width * 0.05

    def flip(self):
        self.direction *= -1

    def draw(self):
        self.surface.fill((0, 0, 0, 0))
        self.sub_surface.fill((0, 0, 0, 0))

        front_light = pygame.Rect(0.85 * self.width + self.width * 0.05, 0.5 * self.height,
                                  0.2 * self.width, 0.5 * self.height)
        back_light = pygame.Rect(0, 0.5 * self.height,
                                 0.2 * self.width, 0.5 * self.height)
        front_light_color = self.COLORS['FRONT_LIGHT_COLOR']
        back_light_color = self.COLORS['BACK_LIGHT_COLOR']

        pygame.draw.ellipse(self.sub_surface, front_light_color, front_light)
        pygame.draw.ellipse(self.sub_surface, back_light_color, back_light)

        lower_part = pygame.Rect(0, 0.5 * self.height, self.width, 0.5 * self.height)
        pygame.draw.rect(self.surface, self.COLORS['CAR_COLOR'], lower_part)

        upper_part_points = [
            (0.3 * self.width, 0),
            (0.7 * self.width, 0),
            (0.8 * self.width, 0.5 * self.height),
            (0.2 * self.width, 0.5 * self.height)
        ]
        pygame.draw.polygon(self.surface, self.COLORS['CAR_COLOR'], upper_part_points)

        wheel_radius = 0.15 * self.width
        wheel1 = pygame.Rect(0.15 * self.width, 0.85 * self.height, wheel_radius, wheel_radius)
        wheel2 = pygame.Rect(0.7 * self.width, 0.85 * self.height, wheel_radius, wheel_radius)
        pygame.draw.ellipse(self.surface, self.COLORS['WHEEL_COLOR'], wheel1)
        pygame.draw.ellipse(self.surface, self.COLORS['WHEEL_COLOR'], wheel2)

        front_window_points = [
            (0.52 * self.width, 0.05 * self.height),
            (0.68 * self.width, 0.05 * self.height),
            (0.77 * self.width, 0.47 * self.height),
            (0.52 * self.width, 0.47 * self.height)
        ]
        pygame.draw.polygon(self.surface, self.COLORS['WINDOWS_COLOR'], front_window_points)

        back_window_points = [
            (0.32 * self.width, 0.05 * self.height),
            (0.48 * self.width, 0.05 * self.height),
            (0.48 * self.width, 0.47 * self.height),
            (0.25 * self.width, 0.47 * self.height)
        ]
        pygame.draw.polygon(self.surface, self.COLORS['WINDOWS_COLOR'], back_window_points)

        handle1 = pygame.Rect(0.3 * self.width, 0.55 * self.height,
                              0.05 * self.width, 0.05 * self.height)
        handle2 = pygame.Rect(0.55 * self.width, 0.55 * self.height,
                              0.05 * self.width, 0.05 * self.height)
        pygame.draw.rect(self.surface, self.COLORS['DETAILS_COLOR'], handle1)
        pygame.draw.rect(self.surface, self.COLORS['DETAILS_COLOR'], handle2)

        if self.direction == -1:
            self.sub_surface.blit(self.surface, (self.width * 0.05, 0))
            flipped_surface = pygame.transform.flip(self.sub_surface, True, False)
            self.main_surface.blit(flipped_surface, (self.x, self.y))
        else:
            self.sub_surface.blit(self.surface, (self.width * 0.05, 0))
            self.main_surface.blit(self.sub_surface, (self.x, self.y))