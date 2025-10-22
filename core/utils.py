import pygame

pygame.init()
pygame.mixer.init()

BACKGROUND = pygame.image.load("assets/star-sky.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (1000, 600))

RUNNING = True
GAME_STATE = "MENU"

DEV_MODE = False

FONT = pygame.font.SysFont("Arial", 30)
CLICK_SOUND = pygame.mixer.Sound("assets/click_sound.wav")
BULLET_SOUND = pygame.mixer.Sound("assets/bullet_sound.wav")
SQUARE_DESTROYED_SOUND = pygame.mixer.Sound("assets/square_destroyed.wav")

PLAY_BTN = FONT.render("Play Game", True, (0, 0, 255))
PLAY_BTN_HOVER = FONT.render("Play Game", True, (0, 255, 255))
PLAY_BTN_HOVER_FLAG = False
PLAY_BTN_RECT = PLAY_BTN.get_rect()
PLAY_BTN_RECT.center = (1000//2 , 500//2)

QUIT_BTN = FONT.render("Quit Game", True, (0, 0, 255))
QUIT_BTN_HOVER = FONT.render("Quit Game", True, (0, 255, 255))
QUIT_BTN_HOVER_FLAG = False
QUIT_BTN_RECT = QUIT_BTN.get_rect()
QUIT_BTN_RECT.center = (1000//2 , 600//2)

PLAYER_IMG = pygame.image.load("assets/star-ship.png")
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (100, 100))
PLAYER_RECT = PLAYER_IMG.get_rect()
PLAYER_RECT.bottomleft = (0, 600)
PLAYER_AREA = pygame.Rect(0, 450, 1000, 150)

BASIC_IMG = pygame.transform.scale(pygame.image.load("assets/enemies/basic.png"), (40, 40))
EVASIVE_IMG = pygame.transform.scale(pygame.image.load("assets/enemies/evasive.png"), (40, 40))
TANK_IMG = pygame.transform.scale(pygame.image.load("assets/enemies/tank.png"), (40, 40))