# core/sound_manager.py
from core.resource import load_sound, load_path
import pygame

class SoundManager:
    _sounds = {}
    _musics = {}
    _volumes = {}
    _active_channels = {}
    _muted = False

    @classmethod
    def init(cls):
        pygame.mixer.init()
        cls.load_sounds()
        cls._muted = False

    @classmethod
    def load_sounds(cls):

        cls._sounds = {
            "click": load_sound("assets", "sounds", "click_sound.wav"),
            "shoot": load_sound("assets", "sounds", "bullet_sound.wav"),
            "enemy_bullet": load_sound("assets", "sounds", "enemy_bullet_sound.wav"),
            "square_death": load_sound("assets", "sounds", "square_destroyed.wav"),
            "burster_death": load_sound("assets", "sounds", "burster_death.wav")
        }

        cls._musics = {
            "main_menu_music": load_path("assets", "music", "main_menu_music.mp3"),
            "game_menu_music": load_path("assets", "music", "game_menu_music.mp3"),
        }

        cls._volumes = {name: 1.0 for name in cls._sounds}

        for name, sound in cls._sounds.items():
            sound.set_volume(cls._volumes.get(name, 1.0))

    @classmethod
    def play(cls, name):
        if cls._muted:
            return
        if name in cls._sounds:
            cls._sounds[name].play()

    @classmethod
    def play_once(cls, name, loops=-1):
        if cls._muted or name not in cls._sounds:
            return
        if name in cls._active_channels:
            ch = cls._active_channels[name]
            if ch.get_busy():
                return
        ch = cls._sounds[name].play(loops=loops)
        cls._active_channels[name] = ch

    @classmethod
    def stop(cls, name):
        if name in cls._sounds:
            cls._sounds[name].stop()
    
    @classmethod
    def fadeout(cls, name, ms=500):
        if name in cls._sounds:
            cls._sounds[name].fadeout(ms)

    @classmethod
    def play_music(cls, name, loops=-1, fade_ms=1000):
        if not cls._muted and name in cls._musics:
            pygame.mixer.music.load(cls._musics[name])
            pygame.mixer.music.play(loops=loops, fade_ms=fade_ms)

    @classmethod
    def set_volume(cls, name, volume):
        if name in cls._sounds:
            cls._volumes[name] = volume
            cls._sounds[name].set_volume(volume)

    @classmethod
    def mute(cls):
        cls._muted = True
        for sound in cls._sounds.values():
            sound.set_volume(0)
        pygame.mixer.music.set_volume(0)

    @classmethod
    def unmute(cls):
        cls._muted = False
        for name, sound in cls._sounds.items():
            sound.set_volume(cls._volumes.get(name, 1.0))
        pygame.mixer.music.set_volume(1.0)
