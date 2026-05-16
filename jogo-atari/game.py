import pygame
import sys
from settings import *
from entities import Player, Asteroid

def draw_text(surf, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont("arial", size, bold=True)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def main():
    # Inicialização do Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jogo Atari - Sobrevivência")
    clock = pygame.time.Clock()

    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()

    # Criar jogador
    player = Player()
    all_sprites.add(player)

    score = 0
    frame_count = 0
    running = True
    game_over = False

    # Loop principal
    while running:
        clock.tick(FPS)
        frame_count += 1

        # 1. Processar Eventos (Input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.shoot(all_sprites, projectiles)
            else:
                # Se for Game Over, pode apertar enter para reiniciar
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_over = False
                        score = 0
                        frame_count = 0
                        
                        # Limpa os grupos
                        all_sprites.empty()
                        asteroids.empty()
                        projectiles.empty()
                        
                        # Recria o jogador
                        player = Player()
                        all_sprites.add(player)

        if not game_over:
            # Lógica de Spawn de Asteroides
            if frame_count % SPAWN_RATE == 0:
                asteroid = Asteroid()
                all_sprites.add(asteroid)
                asteroids.add(asteroid)

            # 2. Atualizar sprites
            all_sprites.update()

            # 3. Verificar Colisões
            
            # Projétil acerta Asteroide (Ambos são destruídos: True, True)
            hits = pygame.sprite.groupcollide(asteroids, projectiles, True, True)
            for hit in hits:
                score += 10 # Aumenta a pontuação
            
            # Asteroide acerta Player (False para não destruir o player de imediato da memória, mas gera Game Over)
            hits_player = pygame.sprite.spritecollide(player, asteroids, False)
            if hits_player:
                game_over = True

            # Asteroide chega no fundo da tela
            for ast in asteroids:
                if ast.rect.bottom >= HEIGHT:
                    game_over = True

        # 4. Renderização (Desenhar tela)
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Desenhar Pontuação
        draw_text(screen, f"Score: {score}", 24, 70, 10, WHITE)

        # Tela de Game Over
        if game_over:
            draw_text(screen, "GAME OVER", 64, WIDTH // 2, HEIGHT // 3, RED)
            draw_text(screen, "Pressione ENTER para jogar novamente", 22, WIDTH // 2, HEIGHT // 2, WHITE)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
