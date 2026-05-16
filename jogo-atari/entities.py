# entities.py
import pygame
import random
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -PLAYER_SPEED
        if keystate[pygame.K_RIGHT]:
            self.speedx = PLAYER_SPEED
        
        self.rect.x += self.speedx
        
        # Manter o jogador dentro das bordas da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self, all_sprites, projectiles):
        projectile = Projectile(self.rect.centerx, self.rect.top)
        all_sprites.add(projectile)
        projectiles.add(projectile)


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ASTEROID_WIDTH, ASTEROID_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        # Nascer em uma posição X aleatória no topo da tela
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        
        # Velocidade aleatória para dar dinamismo
        self.speedy = random.randrange(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)

    def update(self):
        self.rect.y += self.speedy
        # Se saiu pela parte de baixo da tela, destrói e penaliza (a ser gerido no game.py)
        # O gerenciamento de "passar da tela" para dar Game Over fica no loop principal.


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PROJECTILE_WIDTH, PROJECTILE_HEIGHT))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = PROJECTILE_SPEED

    def update(self):
        self.rect.y += self.speedy
        # Se sair da tela (pelo topo), o projétil é destruído para não gastar memória
        if self.rect.bottom < 0:
            self.kill()
