# entities/wave_manager.py
from core.utils import DEMO_WAVE
from waves.demo_wave import Demo_Wave

class WaveManager:
    def __init__(self, scene):
        self.scene = scene
        self.current_wave_number = 1
        self.current_wave = None
        if DEMO_WAVE:
            self.wave_classes = {1: Demo_Wave}
        else:
            self.wave_classes = Demo_Wave.registry

    def start_wave(self, wave_number):
        """Initialize the given wave."""
        if wave_number in self.wave_classes:
            self.current_wave = self.wave_classes[wave_number](self.scene)
            self.current_wave.setup()
            self.scene.ui_manager.on_wave_started(wave_number)
        else:
            self.current_wave = None
            self.end_game()

    def update(self, dt):
        if not self.current_wave: return
        
        self.current_wave.update(dt)
        
        if self.current_wave.is_finished():
            self.current_wave_number += 1
            self.start_wave(self.current_wave_number)
    
    def end_game(self):
        self.scene.manager.fade.start_fade_out(
            on_complete=lambda: self.scene.manager.change_scene("MenuScene")
        )
