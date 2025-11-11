import pygame

class SceneManager:
    def __init__(self, fade):
        self.current_scene = None
        self.fade = fade
        self.scene_registry = {}

    def register_scene(self, name, scene_class):
        self.scene_registry[name] = scene_class

    def change_scene(self, name):
        scene_class = self.scene_registry[name]
        self.current_scene = scene_class(self)

    def handle_events(self, events):
        self.current_scene.handle_events(events)

    def update(self, dt):
        self.current_scene.update(dt)

    def render(self, screen):
        self.current_scene.render(screen)