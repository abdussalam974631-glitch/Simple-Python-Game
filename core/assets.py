# core/assets.py
import pygame

class AssetManager:
    cache = {}

    @staticmethod
    def load_image(path):
        if path not in AssetManager.cache:
            AssetManager.cache[path] = pygame.image.load(path).convert_alpha()
        return AssetManager.cache[path]
