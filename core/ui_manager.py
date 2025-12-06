import pygame

class UIManager:
    def __init__(self, scene):
        self.scene = scene
        self.widgets = []

    def add(self, widget):
        self.widgets.append(widget)

    def update(self, dt):
        for widget in self.widgets:
            widget.update(dt)

    def render(self, screen):
        for widget in self.widgets:
            widget.render(screen)

    def on_score_changed(self, new_score):
        for w in self.widgets:
            if hasattr(w, "set_score"):
                w.set_score(new_score)

    def on_lives_changed(self, new_lives):
        for w in self.widgets:
            if hasattr(w, "set_lives"):
                w.set_lives(new_lives)

    def on_wave_started(self, wave_number):
        for w in self.widgets:
            if hasattr(w, "show_wave"):
                w.show_wave(wave_number)

    def on_pause_changed(self, paused):
        for w in self.widgets:
            if hasattr(w, "set_paused"):
                w.set_paused(paused)
