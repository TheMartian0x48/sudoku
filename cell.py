import pygame


class Cell:
    def __init__(self, x, y, width, fixed, background, foreground):
        self.x = x
        self.y = y
        self.width = width
        self.fixed = fixed
        self.background = background
        self.foreground = foreground

    def draw(self, window, font, val):
        pygame.draw.rect(window, self.background, [self.x, self.y, self.width, self.width])
        if val not in range(1, 10):
            return
        text = font.render(str(val), True, self.foreground)
        window.blit(text, (self.x + 20, self.y + 20))
