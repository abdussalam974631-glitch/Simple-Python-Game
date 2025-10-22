import pygame
from core.utils import *
from entities.player import Player
from entities.wave_manager import WaveManager


class GameScene:
    def __init__(self, manager):
        self.manager = manager  # Reference to the scene manager
        self.mouse_pos = pygame.mouse.get_pos()
        self.manager.fade.start_fade_in()

        self.player = Player()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(self.player)

        self.SCORE = 0
        self.LIVES = 5
        self.paused = False
        self.wave_manager = WaveManager(self)


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                
                if not self.paused:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot(self.bullets, self.all_sprites)
            
            if not self.paused:
                pass


    def update(self, dt):
        
        if self.paused:
            return
        else:

            self.wave_manager.update(dt)
            
            for enemy in list(self.enemies):
                if enemy.health == 0:
                    enemy.kill()
                    SQUARE_DESTROYED_SOUND.play()
                    self.SCORE += 10

                if enemy.rect.bottom > 450:
                    enemy.kill()
                    SQUARE_DESTROYED_SOUND.play()
                    self.LIVES = max(self.LIVES - 1, 0)
                    if self.LIVES <= 0:
                        self.manager.fade.start_fade_out(on_complete=lambda:self.manager.change_scene("MenuScene"))

            hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True)
            for enemy, bullets_hit in hits.items():
                enemy.health -= len(bullets_hit)
                
            
            self.all_sprites.update(dt)


        

    def render(self, screen):
        screen.blit(BACKGROUND, (0,0))
        self.all_sprites.draw(screen)

        text = pygame.font.Font(None, 36)
        score_text = text.render(f"Score: {self.SCORE}", True, (255, 255, 255))
        lives_text = text.render(f"Lives: {self.LIVES}", True, (255, 255, 255))
        wave_text = text.render(f"Waves: {self.wave_manager.current_wave}", True, (255, 255, 255))
        rem_text = text.render(f"Remaining: {self.wave_manager.total_to_spawn() - self.wave_manager.total_spawned()}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 40))
        screen.blit(wave_text, (10, 70))
        screen.blit(rem_text, (10, 100))

        if self.paused:
            # Create semi-transparent gray overlay
            overlay = pygame.Surface((screen.get_width(), screen.get_height()))
            overlay.set_alpha(150)  # 0 = fully transparent, 255 = opaque
            overlay.fill((50, 50, 50))  # Dark gray color
            screen.blit(overlay, (0, 0))

            # Optional: draw text
            font = pygame.font.Font(None, 48)
            text = font.render("Paused", True, (255, 255, 255))
            screen.blit(text, (screen.get_width()//2 - text.get_width()//2, screen.get_height()//2 - text.get_height()//2))

        self.manager.fade.update(screen)