import os
import sys
import pygame

# Works for both Python and PyInstaller EXE
BASE_PATH = getattr(sys, "_MEIPASS", os.path.abspath("."))

def load_image(*path_parts):
    """Load an image using PyInstaller-safe path"""
    return pygame.image.load(os.path.join(BASE_PATH, *path_parts))

def load_sound(*path_parts):
    return pygame.mixer.Sound(os.path.join(BASE_PATH, *path_parts))

def load_font(*path_parts, size=24):
    return pygame.font.Font(os.path.join(BASE_PATH, *path_parts), size)

def load_path(*path_parts):
    return os.path.join(BASE_PATH, *path_parts)
