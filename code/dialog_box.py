import pygame


class Dialog_Box:
    def __init__(self, screen):
        self.reading = False

        self.screen = screen

        self.pannel_width = self.screen.get_size()[0] // 1.2
        self.pannel_height = self.screen.get_size()[1] // 5
        self.pannel_pos = self.screen.rect.midbottom

        self.pannel = pygame.transform.scale(pygame.image.load("../assets/dialogs/dialog box.png"),
                                             (self.pannel_width, self.pannel_height))

        self.font = pygame.font.Font("../assets/dialogs/PokemonDS.ttf", 18)

        self.texts = []
        self.txt_idx = 0

    def render(self):
        if self.reading:
            self.screen.display.blit(self.pannel, (self.pannel_pos[0] - self.pannel_width // 2,
                                                   self.pannel_pos[1] - self.pannel_height - 30))

    def next_text(self):
        self.screen.display.blit(self.texts[self.txt_idx], (0, 0))

        self.txt_idx += 1
        if self.txt_idx >= len(self.texts):
            self.txt_idx = 0
            self.reading = False

