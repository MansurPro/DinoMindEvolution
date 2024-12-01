import pygame
import random
import sys
import math
from enum import Enum

# Game settings
width = 1280
height = 720
bg = (255, 255, 255, 255)

score = 0
score_speedup = 100
game_speed = 8.0
skins = ["default", "aqua", "black", "bloody", "cobalt", "gold", "insta",
         "lime", "magenta", "magma", "navy", "neon", "orange", "pinky",
         "purple", "rgb", "silver", "subaru", "sunny", "toxic"]
names = ["Fluffinator", "Falafel King", "Witchlord", "Dandyflower", "Googly-Eyes", "Slimey", 
         "Zoomer", "Trailblazer", "Tiny Titan", "Subaru-Chan", "T-Rexington", "Featherling", 
         "Private Snuggles", "The Wise One", "Captain Veteran", "Pixel Knight", 
         "Ronin", "Nomad"]


class DinoState(Enum):
    RUN = 1
    JUMP = 2


class Dino:
    def __init__(self, x, y, color="default", name="Player"):
        self.color = color
        self.name = name
        self.state = DinoState.RUN
        self.jump_power = 10
        self.cur_jump_power = self.jump_power
        self.load_sprites()
        self.hitbox = pygame.Rect(x, y, self.sprites["run"][0].get_width(), self.sprites["run"][0].get_height())
        self.image = self.sprites["run"][0]
        self.run_animation_index = [0, 5]

    def load_sprites(self):
        self.sprites = {"run": [], "jump": []}
        self.sprites["jump"].append(pygame.image.load(f"sprites/dino/{self.color}_jump.png"))
        self.sprites["run"].append(pygame.image.load(f"sprites/dino/{self.color}_run1.png"))
        self.sprites["run"].append(pygame.image.load(f"sprites/dino/{self.color}_run2.png"))

    def update(self):
        if self.state == DinoState.RUN:
            self.run()
        elif self.state == DinoState.JUMP:
            self.jump()

    def run(self):
        self.image = self.sprites["run"][self.run_animation_index[0] // self.run_animation_index[1]]
        self.run_animation_index[0] += 1
        if self.run_animation_index[0] >= self.run_animation_index[1] * 2:
            self.run_animation_index[0] = 0

    def jump(self):
        if self.state == DinoState.JUMP:
            self.hitbox.y -= self.cur_jump_power * (2 * (game_speed / 8))
            self.cur_jump_power -= 0.5 * (game_speed / 8)
            if self.hitbox.y >= height - 170:
                self.hitbox.y = height - 170
                self.state = DinoState.RUN
                self.cur_jump_power = self.jump_power
        else:
            self.state = DinoState.JUMP
            self.image = self.sprites["jump"][0]

    def draw(self, scr, fnt=None):
        scr.blit(self.image, (self.hitbox.x, self.hitbox.y))
        if fnt is not None:
            c_label = fnt.render(self.name.capitalize(), True, (100, 100, 100))
            c_label_rect = c_label.get_rect()
            c_label_rect.center = (self.hitbox.x + 45, self.hitbox.y - 30)
            scr.blit(c_label, c_label_rect)


class Cactus:
    def __init__(self, x, y, forced_type=None):
        self.available_types = ["1", "2", "3", "4", "5", "6"]
        self.cactus_type = forced_type if forced_type else random.choice(self.available_types)
        self.image = pygame.image.load(f"sprites/cactus/{self.cactus_type}.png")
        self.hitbox = self.image.get_rect(topleft=(x, y - self.image.get_height()))
        self.is_active = True

    def update(self):
        self.hitbox.x -= game_speed
        if self.hitbox.right < 0:
            self.is_active = False

    def draw(self, scr):
        scr.blit(self.image, self.hitbox)


def run_game():
    global game_speed, score, score_speedup

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Roboto Condensed", 30)
    score_font = pygame.font.SysFont("Roboto Condensed", 40)

    dino = Dino(30, height - 170, "default", "Player")
    enemies = [Cactus(width + 300, height - 85)]
    road_chunks = [
        [pygame.image.load('sprites/road.png'), [0, height - 100]],
        [pygame.image.load('sprites/road.png'), [2404, height - 100]]
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and dino.state != DinoState.JUMP:
            dino.jump()

        # Game logic
        dino.update()
        for enemy in enemies:
            enemy.update()
            if dino.hitbox.colliderect(enemy.hitbox):
                running = False  # End the game on collision

        # Remove inactive enemies
        enemies = [enemy for enemy in enemies if enemy.is_active]

        # Add new enemies
        if len(enemies) < 3:
            enemies.append(Cactus(enemies[-1].hitbox.x + random.randint(200, 600), height - 85))

        # Update score and speed
        score += 0.1
        if score > score_speedup:
            score_speedup += 100
            game_speed += 1

        # Draw everything
        screen.fill(bg)
        for road_chunk in road_chunks:
            road_chunk[1][0] -= game_speed
            if road_chunk[1][0] <= -2400:
                road_chunk[1][0] = road_chunks[1][1][0] + 2400
            screen.blit(road_chunk[0], road_chunk[1])

        dino.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        # Display score
        score_label = score_font.render(f"Score: {int(score)}", True, (0, 0, 0))
        screen.blit(score_label, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run_game()
