import pygame

from entity import Entity
from tool import controller
from keylistener import Keylistener


class Player(Entity):
    def __init__(self, name, team, spritesheet, x, y):
        super().__init__(name, team, spritesheet, x, y)

        self.spritesheet_walk = self.spritesheet
        self.spritesheet_run = pygame.image.load("../assets/spritesheets/" + spritesheet + "_run.png")
        self.spritesheet_bicycle = pygame.image.load("../assets/spritesheets/" + spritesheet + "_cycle_roll.png")

        self.backpack = {"Items": [], "Balls": [], "CT & CS": [], "Berries": [], "Rare Items": []}
        self.pokedollars = 0

        self.controller = controller
        self.inputs = Keylistener()

        self.interaction = False

    def update(self):
        self.check_inputs()
        super().update()

    def check_inputs(self):
        if not self.in_motion:
            if self.inputs.key_pressed(self.controller["up"]):
                self.move("up")
            elif self.inputs.key_pressed(self.controller["down"]):
                self.move("down")
            elif self.inputs.key_pressed(self.controller["left"]):
                self.move("left")
            elif self.inputs.key_pressed(self.controller["right"]):
                self.move("right")

            if not self.bike:
                self.switch_walk()

            if self.inputs.key_pressed(self.controller["run"]):
                self.switch_run()

            if self.inputs.key_pressed(self.controller["bike"]):
                self.inputs.remove_key(self.controller["bike"])
                self.switch_bike()

            self.interaction = False
            if self.inputs.key_pressed(self.controller["interact"]):
                self.inputs.remove_key(self.controller["interact"])
                self.interaction = True

    def switch_walk(self):
        if not self.position.x % 2 and not self.position.y % 2:
            self.speed = 1
            self.active_spritesheet = self.spritesheet_walk

    def switch_run(self):
        if not self.bike:
            if self.in_motion:
                self.speed = 2
                self.active_spritesheet = self.spritesheet_run

    def switch_bike(self):
        if not self.bike:
            self.bike = True
            self.speed = 4
            self.active_spritesheet = self.spritesheet_bicycle
        elif self.bike:
            self.bike = False
            self.speed = 1
            self.active_spritesheet = self.spritesheet_walk
