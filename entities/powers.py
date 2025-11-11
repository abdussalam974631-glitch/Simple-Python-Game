# entities/powers.py
import pygame

class PowerUp:

    def __init__(self, duration=0):
        self.duration = duration
        self.start_time = None
        self.active = False

    def apply(self, player):
        self.start_time = pygame.time.get_ticks()
        self.active = True
        self.on_apply(player)

    def update(self, player):
        
        if self.duration and pygame.time.get_ticks() - self.start_time > self.duration:
            self.on_remove(player)
            return False
        return True

    def on_apply(self, player): pass
    def on_remove(self, player): pass


class RapidFire(PowerUp):
    def __init__(self):
        super().__init__(duration=5000)  

    def on_apply(self, player):
        player.shoot_delay /= 2  

    def on_remove(self, player):
        player.shoot_delay *= 2  


class ExtraLife(PowerUp):
    def __init__(self):
        super().__init__(duration=0)  

    def on_apply(self, player):
        player.lives = min(player.lives+ 1, 5)
