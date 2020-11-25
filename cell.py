import pygame


class Cell:
    def __init__(self, x, y, width, height, fixed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected = False
        self.fixed = fixed

    def draw(self, win, font, val):
        pygame.draw.rect(win, (255, 255, 255), [
                         self.x, self.y, self.width, self.height])
        if val == -1:
            return
        color = (0, 255, 0)
        if self.fixed == True:
            color = (181, 154, 4)
        text = font.render(str(val), True, color)
        win.blit(text, (self.x + 20, self.y + 20))
