import pygame

class CollisionSystem:
    def __init__(self, scene):
        self.scene = scene

    def update(self):
        self.player_bullet_hits_enemy()
        self.enemy_bullet_hits_player()
        self.player_hits_powerups()
        self.enemies_reach_bottom()
        self.enemies_hits_player()


    def player_bullet_hits_enemy(self):
        hits = pygame.sprite.groupcollide(
            self.scene.enemies,
            self.scene.bullets,
            False,
            True,
            pygame.sprite.collide_mask
        )
        for enemy, bullets in hits.items():
            enemy.take_damage(len(bullets))


    def enemy_bullet_hits_player(self):
        hits = pygame.sprite.spritecollide(
            self.scene.player,
            self.scene.enemy_bullets,
            True,
            pygame.sprite.collide_mask
        )
        if hits:
            self.scene.player.take_damage()


    def player_hits_powerups(self):
        hits = pygame.sprite.spritecollide(
            self.scene.player,
            self.scene.powers,
            True,
            pygame.sprite.collide_mask
        )
        for power in hits:
            power.apply_to_player(self.scene.player)


    def enemies_reach_bottom(self):
        for enemy in list(self.scene.enemies):
            if enemy.rect.bottom >= 600:
                self.scene.player.take_damage()
                enemy.kill()
    
    def enemies_hits_player(self):
        hits = pygame.sprite.groupcollide(
            self.scene.enemies,
            pygame.sprite.GroupSingle(self.scene.player),
            True,
            False,
            pygame.sprite.collide_mask
        )
        if hits:
            self.scene.player.take_damage()
