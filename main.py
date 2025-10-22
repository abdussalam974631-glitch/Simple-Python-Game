import pygame
from core.SceneManager import SceneManager
from scenes import GameState, MenuState
from core.fade_transition import FadeTransition
from core.utils import *
import core.utils

pygame.init()
pygame.mixer.init()

DISPLAY_WIDTH = 1000
screen = pygame.display.set_mode((DISPLAY_WIDTH, 600))
pygame.display.set_caption("Simple Game")

pygame.mixer.music.load("assets/music-background.mp3")
pygame.mixer.music.play()

clock = pygame.time.Clock()

dt = clock.tick(60)    
fade = FadeTransition(1000, 600, 1)

scene = SceneManager(fade)
scene.register_scene( "MenuScene", MenuState.MenuScene)
scene.register_scene("GameScene", GameState.GameScene)
scene.change_scene("MenuScene")

if core.utils.DEV_MODE: scene.change_scene("GameScene")

while core.utils.RUNNING:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            core.utils.RUNNING = False

    scene.handle_events(events)
    scene.update(dt)
    scene.render(screen)
    

    pygame.display.flip()
    clock.tick(60)