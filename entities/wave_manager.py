# entities/wave_manager.py
import pygame
from core.enemy_factory import EnemyFactory

class WaveManager:
    def __init__(self, game_scene):
        self.scene = game_scene
        self.enemy_factory = EnemyFactory()
        self.current_wave = 1
        self.wave_data = self.get_wave_data(self.current_wave)
        self.spawn_delay = 1000
        self.last_spawn_time = 0
        self.spawn_progress = {etype: 0 for etype, _ in self.wave_data}
        self.wave_active = True

    def get_wave_data(self, wave_number):
        if wave_number == 1:
            return [("basic", 10)]
        elif wave_number == 2:
            return [("basic", 5), ("evasive", 5)]
        elif wave_number == 3:
            return [("evasive", 8), ("tank", 2)]
        elif wave_number == 4:
            return [("tank", 4), ("evasive", 6)]
        else:
            return [("basic", 3), ("evasive", 3), ("tank", 2)]

    def update(self, dt):
        now = pygame.time.get_ticks()
        if not self.wave_active:
            return

        # Spawn based on time
        if now - self.last_spawn_time > self.spawn_delay:
            self.spawn_next_enemy()
            self.last_spawn_time = now

        # Check wave completion
        if not self.scene.enemies and self.total_spawned() >= self.total_to_spawn():
            self.start_next_wave()

    def spawn_next_enemy(self):
        """Spawn enemies one at a time in sequence from the wave data."""
        for enemy_type, count in self.wave_data:
            if self.spawn_progress[enemy_type] < count:
                enemy = self.enemy_factory.create_enemy(enemy_type)
                self.scene.enemies.add(enemy)
                self.scene.all_sprites.add(enemy)
                self.spawn_progress[enemy_type] += 1
                break  # spawn one per update cycle

    def total_to_spawn(self):
        return sum(count for _, count in self.wave_data)

    def total_spawned(self):
        return sum(self.spawn_progress.values())

    def start_next_wave(self):
        self.current_wave += 1
        self.wave_data = self.get_wave_data(self.current_wave)
        self.spawn_progress = {etype: 0 for etype, _ in self.wave_data}
        self.wave_active = True
        print(f"🌊 Starting wave {self.current_wave}")
