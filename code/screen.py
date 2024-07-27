import pygame


class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((1280, 720))

        self.clock = pygame.time.Clock()
        self.framerate = 60

        self.rect = pygame.Rect(0, 0, self.get_size()[0], self.get_size()[1])

    def update(self):
        pygame.display.flip()
        self.clock.tick(self.framerate)

    def get_size(self):
        return self.display.get_size()

    def get_display(self):
        return self.display
