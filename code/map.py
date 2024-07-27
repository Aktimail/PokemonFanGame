import pygame
import pytmx
import pyscroll

from npc import NPC
from tool import ALL_DIALOGS, ALL_FIGHTERS, ENTITIES_DESTINATIONS


class Map:
    def __init__(self, screen):
        self.screen = screen
        self.player = None

        self.map_name = None
        self.tmx_data = None
        self.map_layer = None
        self.group = None

        self.collisions = []
        self.spawns = []
        self.switches = []
        self.npcs = []

        self.gate = None

        self.map_zoom = 4

        self.rest = False
        self.current_dialogs = []

    def update(self):
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.display)

        self.check_object()

    def switch_map(self, map):
        self.map_name = map
        self.tmx_data = pytmx.load_pygame("../assets/maps/" + self.map_name + ".tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.display.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=50)
        self.map_layer.zoom = self.map_zoom

        self.init_object()
        self.init_npcs()

        if self.gate:
            for spawn in self.spawns:
                if spawn["provenance"] == self.gate["destination"] and spawn["port"] == self.gate["port"]:
                    self.add_player(self.player)
                    self.player.position = spawn["position"]

    def init_object(self):
        self.collisions.clear()
        self.spawns.clear()
        self.switches.clear()
        self.npcs.clear()
        ENTITIES_DESTINATIONS.clear()

        for obj in self.tmx_data.objects:
            if obj.type == "collision":
                self.collisions.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "spawn":
                self.spawns.append({"position": pygame.Vector2(obj.x, obj.y),
                                    "provenance": obj.name.split(" ")[1],
                                    "port": obj.name.split(" ")[2]
                                    })
            if obj.type == "switch":
                self.switches.append({"rect": pygame.Rect(obj.x, obj.y, obj.width, obj.height),
                                      "destination": obj.name.split(" ")[1],
                                      "port": obj.name.split(" ")[2]
                                      })
            if obj.type == "npc":
                self.npcs.append(NPC(obj.name.split(" ")[0], [], obj.name.split(" ")[1], obj.x, obj.y,
                                     obj.name.split(" ")[2]))

    def init_npcs(self):
        for npc in self.npcs:
            self.add_npc(npc)
            if npc.name in ALL_DIALOGS[self.map_name]:
                npc.dialogs = ALL_DIALOGS[self.map_name][npc.name]
            if npc.name in ALL_FIGHTERS[self.map_name]:
                npc.team = ALL_FIGHTERS[self.map_name][npc.name]

        for obj in self.tmx_data.objects:
            if obj.type == "npc path":
                for npc in self.npcs:
                    if npc.name == obj.name.split(" ")[0]:
                        npc.checkpoints[int(obj.name.split(" ")[1])] = pygame.Rect(obj.x, obj.y, 16, 16)

    def check_object(self):
        self.player.collision = False

        for collision in self.collisions:
            if self.player.facing_tile.colliderect(collision):
                self.player.collision = True

        for npc in self.npcs:
            npc.collision = False
            if self.player.facing_tile.colliderect(npc.hitbox):
                self.player.collision = True
            if npc.facing_tile.colliderect(self.player.hitbox):
                npc.collision = True

            self.check_interactions(npc)

        for switch in self.switches:
            if self.player.hitbox.colliderect(switch["rect"]):
                if self.player.step_progression > 12:
                    self.gate = switch
                    self.switch_map(switch["destination"])

    def check_interactions(self, npc):
        if not self.player.in_motion and not npc.in_motion:
            if npc.talking and npc.direction == npc.facing_player(self.player):
                self.rest = True
            if self.player.interaction:
                if self.player.facing_tile.colliderect(npc.hitbox):
                    npc.facing_player(self.player)
                    npc.talking = True
                    self.current_dialogs = npc.dialogs


    def add_player(self, player):
        self.player = player
        self.group.add(player)
        self.player.reset_move()

    def add_npc(self, npc):
        self.group.add(npc)
        npc.reset_move()
