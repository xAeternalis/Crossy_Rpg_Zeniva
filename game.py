import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy


class Game:

    def __init__(self):

        self.width = 800
        self.height = 800
        self.white_colour = (255, 255, 255)
        self.clock = pygame.time.Clock()

        # background = pygame.image.load("assets/background.png")
        self.background = GameObject(0, 0, self.width, self.height, "assets/background.png")

        # treasure = pygame.image.load("assets/treasure.png")
        self.treasure = GameObject(375, 50, 50, 50, "assets/treasure.png")

        self.game_window = pygame.display.set_mode((self.width, self.height))

        self.player = Player(375, 700, 50, 50, 'assets/player.png', 10)
        self.enemies = [
            Enemy(0, 600, 50, 50, 'assets/enemy.png', 10),
            Enemy(750, 400, 50, 50, 'assets/enemy.png', 10),
            Enemy(0, 200, 50, 50, 'assets/enemy.png', 10)
        ]

    def draw_objects(self):
        self.game_window.fill(self.white_colour)

        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))

        pygame.display.update()

    def detecting_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False
        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False

        return True

    def move_objects(self, player_direction):
        self.player.move(player_direction, self.height)
        for enemy in self.enemies:
            enemy.move(self.width)

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detecting_collision(self.player, enemy):
                return True
        if self.detecting_collision(self.player, self.treasure):
            return True
        return False

    def run_game_loop(self):
        player_direction = 0

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0

            self.move_objects(player_direction)
            self.player.move(player_direction, self.height)
            for enemy in self.enemies:
                enemy.move(self.width)
            self.draw_objects()

            if self.check_if_collided():
                return

            self.clock.tick(60)
