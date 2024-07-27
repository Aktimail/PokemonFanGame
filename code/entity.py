import pygame

from tool import split_spritesheet, delay_print, ENTITIES_DESTINATIONS
from pokemon import Pokemon


class Entity(pygame.sprite.Sprite):
    def __init__(self, name, team, spritesheet, x, y):
        super().__init__()

        self.name = name
        self.team: list[Pokemon] = team
        self.lead = self.team[0] if self.team else None
        self.opponent = None

        self.spritesheet = pygame.image.load("../assets/spritesheets/" + spritesheet + ".png")
        self.active_spritesheet = self.spritesheet

        self.position = pygame.math.Vector2(x, y)

        self.in_motion = False
        self.reserve_next_tile = True
        self.direction = "down"
        self.step_progression = 0
        self.speed = 1
        self.facing_tile = pygame.Rect(0, 0, 16, 16)

        self.still_counter = 0

        self.sprite_idx = 0
        self.anim_cycle = 0

        self.collision = False

        self.image = split_spritesheet(self.active_spritesheet)[self.direction][self.sprite_idx]
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(0, 0, 16, 16)

        self.bike = False

    def update(self):
        self.hitbox.topleft = self.position
        self.rect.midbottom = self.hitbox.midbottom
        self.image = split_spritesheet(self.active_spritesheet)[self.direction][self.sprite_idx]
        self.movement_update()
        self.facing_tile_update()
        self.animation_cycle()

    def fight(self):
        pass

    def switch(self, pkmn):
        lead = self.lead
        delay_print((lead.name + " switch with " + pkmn.name))
        idx_pkmn = self.team.index(pkmn)
        lead.boosts = {"atk": 0, "deff": 0, "aspe": 0, "dspe": 0, "spd": 0}
        self.team[0], self.team[idx_pkmn] = self.team[idx_pkmn], self.team[0]
        self.lead = pkmn
        return lead.name, pkmn.name

    def lost(self):
        for pkmn in self.team:
            if not pkmn.ko:
                return False
        return True

    def reset_move(self):
        self.in_motion = False
        self.step_progression = 0
        while self.position.x % 16:
            self.position.x -= 1
        while self.position.y % 16:
            self.position.y -= 1

    def move(self, direction):
        if not self.in_motion:
            if self.direction == direction:
                if not self.collision:
                    if self.grid_check():
                        self.in_motion = True
            else:
                self.direction = direction

    def movement_update(self):
        if self.in_motion:
            self.step_progression += self.speed
            if self.direction == "left":
                self.position.x -= self.speed
            elif self.direction == "right":
                self.position.x += self.speed
            elif self.direction == "up":
                self.position.y -= self.speed
            elif self.direction == "down":
                self.position.y += self.speed

            if self.step_progression >= 16:
                self.step_progression = 0
                self.in_motion = False

    def animation_cycle(self):
        if self.in_motion:
            self.anim_cycle += 1
            if not self.anim_cycle % 8:
                self.sprite_idx += 1

            if self.sprite_idx > 3:
                self.sprite_idx = 0
            if self.anim_cycle >= 16:
                self.anim_cycle = 0

        if not self.in_motion:
            self.still_counter += 1
        if self.still_counter >= 2:
            if self.sprite_idx % 2:
                self.sprite_idx += 1
                if self.sprite_idx > 3:
                    self.sprite_idx = 0
            self.still_counter = 0

    def facing_tile_update(self):
        self.facing_tile.topleft = self.position
        if self.direction == "left":
            self.facing_tile.x -= 16
        if self.direction == "right":
            self.facing_tile.x += 16
        if self.direction == "up":
            self.facing_tile.y -= 16
        if self.direction == "down":
            self.facing_tile.y += 16

    def grid_check(self):
        if not (self.facing_tile.x, self.facing_tile.y) in ENTITIES_DESTINATIONS.values():
            ENTITIES_DESTINATIONS[self.name] = (self.facing_tile.x, self.facing_tile.y)
            return True
        return False
