import pygame
from .sprite_loader import load_frames
from .resource import load_image

pygame.mixer.init()

DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 600

BACKGROUND = load_image("assets", "star-sky.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (1000, 600))

RUNNING = True
DEV_MODE = False
DEMO_WAVE = False

FONT = pygame.font.SysFont("Arial", 30)
FONT_DUBAI = pygame.font.SysFont("dubai", 30)

PLAY_BTN = FONT.render("Play Game", True, (0, 0, 255))
PLAY_BTN_HOVER = FONT.render("Play Game", True, (0, 255, 255))
PLAY_BTN_RECT = PLAY_BTN.get_rect()
PLAY_BTN_RECT.center = (1000//2 , 500//2)

HELP_BTN = FONT.render("Help", True, (0, 0, 255))
HELP_BTN_HOVER = FONT.render("Help", True, (0, 255, 255))
HELP_BTN_RECT = HELP_BTN.get_rect()
HELP_BTN_RECT. center = (1000//2 , 600//2)

QUIT_BTN = FONT.render("Quit Game", True, (0, 0, 255))
QUIT_BTN_HOVER = FONT.render("Quit Game", True, (0, 255, 255))
QUIT_BTN_RECT = QUIT_BTN.get_rect()
QUIT_BTN_RECT.center = (1000//2 , 700//2)

PLAYER_STATES = {
    5: load_frames(load_image("assets", "star-ship", "Main Ship - Base - Full health.png"), 48, 48, (100, 100)),
    4: load_frames(load_image("assets", "star-ship", "Main Ship - Base - Slight damage.png"), 48, 48, (100, 100)),
    3: load_frames(load_image("assets", "star-ship", "Main Ship - Base - Damaged.png"), 48, 48, (100, 100)),
    2: load_frames(load_image("assets", "star-ship", "Main Ship - Base - Very damaged.png"), 48, 48, (100, 100)),
    1: load_frames(load_image("assets", "star-ship", "Main Ship - Base - Very damaged.png"), 48, 48, (100, 100))
    }

PLAYER_AREA = pygame.Rect(0, 250, 1000, 350)
BULLET_FRAMES = load_frames(load_image("assets", "bullet", "bullet.png"), 32, 32)

Animations = {
    "basic": load_frames(load_image("assets", "enemies", "BASIC.png"), 48, 48, (48, 48)),
    "evasive": load_frames(load_image("assets", "enemies", "EVASIVE.png"), 48, 48, (48, 48)),
    "tank": load_frames(load_image("assets", "enemies", "TANK.png"), 48, 48, (48, 48)),
    "shooter": load_frames(load_image("assets", "enemies", "SHOOTER.png"), 48, 48, (48, 48)),
    "doppelganger": load_frames(load_image("assets", "enemies", "DOPPELGANGER.png"), 48, 48, (48, 48)),
    "burster": load_frames(load_image("assets", "enemies", "BURSTER.png"), 48, 48, (48, 48)),
    "orbiter": load_frames(load_image("assets", "enemies", "ORBITER.png"), 48, 48, (48, 48)),
    "serpenthead": load_frames(load_image("assets", "enemies", "SERPENT.png"), 48, 48, (48, 48)),
    "serpentsegment": load_frames(load_image("assets", "enemies", "SERPENTSEG.png"), 48, 48, (48, 48)),
    "cloaker": load_frames(load_image("assets", "enemies", "CLOAKER.png"), 48, 48, (48, 48))
}

RAPIDFIRE_IMG = pygame.Surface((40, 40), pygame.SRCALPHA)
pygame.draw.circle(RAPIDFIRE_IMG, (0, 0, 255), (15, 15), 13)

HEALTH_IMG = pygame.Surface((40, 40), pygame.SRCALPHA)
pygame.draw.circle(HEALTH_IMG, (255, 0, 0), (15, 15), 13)
