# core/enemy_factory.py
import random
from entities.enemies import *
from .enemy_config import ENEMY_TYPES

class EnemyFactory:

    @staticmethod
    def create_enemy(type_name, x=None, y=None):
        enemy = ENEMY_TYPES[type_name]()
        return enemy

    @staticmethod
    def get_random_enemy():
        type_name = random.choice(list(ENEMY_TYPES.keys()))
        return EnemyFactory.create_enemy(type_name)
