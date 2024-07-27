import pygame

from entity import Entity


class NPC(Entity):
    def __init__(self, name, team, spritesheet, x, y, direction):
        super().__init__(name, team, spritesheet, x, y)

        self.direction = direction

        self.checkpoints = {1: pygame.Rect(self.position.x, self.position.y, 16, 16)}
        self.checkpoint_idx = 1

        self.talking = False
        self.dialogs = []

    def update(self):
        self.auto_move()
        super().update()

    def auto_move(self):
        if not self.talking:
            cc_idx = self.checkpoint_idx
            nc_idx = self.checkpoint_idx + 1

            if nc_idx > len(self.checkpoints):
                nc_idx = 1

            current_checkpoint = self.checkpoints[cc_idx]
            next_checkpoint = self.checkpoints[nc_idx]

            if current_checkpoint.y - next_checkpoint.y > 0:
                self.move("up")
            elif current_checkpoint.y - next_checkpoint.y < 0:
                self.move("down")
            elif current_checkpoint.x - next_checkpoint.x > 0:
                self.move("left")
            elif current_checkpoint.x - next_checkpoint.x < 0:
                self.move("right")

            if self.hitbox.colliderect(next_checkpoint):
                self.checkpoint_idx = nc_idx

    def facing_player(self, player):
        if not self.in_motion:
            if player.position.x - self.position.x > 0:
                self.direction = "right"
            if player.position.x - self.position.x < 0:
                self.direction = "left"
            if player.position.y - self.position.y > 0:
                self.direction = "down"
            if player.position.y - self.position.y < 0:
                self.direction = "up"
            return self.direction
