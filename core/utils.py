import pygame

pygame.init()
pygame.mixer.init()

DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 600

BACKGROUND = pygame.image.load("assets/star-sky.jpg")
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

PLAYER_IMG = pygame.transform.scale(pygame.image.load("assets/star-ship.png"), (100, 100))
PLAYER_RECT = PLAYER_IMG.get_rect()
PLAYER_RECT.bottomleft = (0, 600)
PLAYER_AREA = pygame.Rect(0, 450, 1000, 150)

BASIC_IMG = pygame.transform.scale(pygame.image.load("assets/enemies/basic.png"), (40, 40))
EVASIVE_IMG = pygame.transform.scale(pygame.image.load("assets/enemies/evasive.png"), (40, 40))
TANK_IMG = pygame.transform.scale(pygame.image.load("assets/enemies/tank.png"), (40, 40))
SHOOTER_IMG = pygame.transform.scale(pygame.image.load("assets/enemies/shooter.png"), (40, 40))
DOPPELGANGER_IMG = pygame.transform.scale(pygame.image.load("assets/enemies/doppelganger.png"), (40, 40))

RAPIDFIRE_IMG = pygame.Surface((40, 40), pygame.SRCALPHA)
pygame.draw.circle(RAPIDFIRE_IMG, (0, 0, 255), (15, 15), 13)

HEALTH_IMG = pygame.Surface((40, 40), pygame.SRCALPHA)
pygame.draw.circle(HEALTH_IMG, (255, 0, 0), (15, 15), 13)
