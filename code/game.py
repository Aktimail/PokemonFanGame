from screen import Screen
from map import Map
from player import Player
from entity import *
from dialog_box import Dialog_Box


class Game:
    def __init__(self):
        self.running = True

        self.screen = Screen()
        self.dialog_box = Dialog_Box(self.screen)
        self.map = Map(self.screen)
        self.player = Player("Red", [], "hero_01", 800, 800)

        self.map.switch_map("Saint-Rémy")
        self.map.add_player(self.player)

    def input_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.player.inputs.add_key(event.key)
            elif event.type == pygame.KEYUP:
                self.player.inputs.remove_key(event.key)

    def dialogs_handler(self):
        self.dialog_box.texts = self.map.current_dialogs

    def run(self):
        while self.running:
            self.screen.update()
            self.map.update()
            self.dialog_box.render()

            self.input_handler()
            self.dialogs_handler()
