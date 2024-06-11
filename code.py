#!/usr/bin/env python3

# Created by: Kaitlyn I and Ava V
# Created on: June 2024
# This constants file is for Space Alien game

import time
import random
import stage
import supervisor
import ugame
import constants

from scenes import SplashScene, MenuScene, GameScene, GameOverScene

class SpaceAliensGame:
    def __init__(self):
        self.sound = ugame.audio


    def splash_scene(self):
        scene = SplashScene(self)
        scene.run()


    def menu_scene(self):
        scene = MenuScene(self)
        scene.run()

    def game_scene(self):
        scene = GameScene(self)
        scene.run()

    def game_over_scene(self, score):
        scene = GameOverScene(self, score)
        scene.run()
