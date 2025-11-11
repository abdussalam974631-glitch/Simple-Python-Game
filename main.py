import pygame
from core.sound_manager import SoundManager
from core.scenemanager import SceneManager
from scenes import GameState, MenuState, HelpState
from core.fade_transition import FadeTransition
from core.utils import *
import core.utils

pygame.init()
SoundManager.load_sounds()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Simple Game")

clock = pygame.time.Clock()

dt = clock.tick(60)
fade = FadeTransition(1000, 600, 1)

scene = SceneManager(fade)
scene.register_scene("MenuScene", MenuState.MenuScene)
scene.register_scene("GameScene", GameState.GameScene)
scene.register_scene("HelpScene", HelpState.HelpScene)

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