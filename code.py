#!/usr/bin/env python3


# Created by: Ava V and Kaitlyn I
# Created on: Mar 2023
# This program is the "space alien" game on pybadge


import stage
import ugame
import random
import time
import supervisor


import constants

import pygame
from splash_scene import SplashScene
from game_over_scene import GameOverScene
from menu_scene import MenuScene
from game_scene import GameScene

splash_scene = SplashScene()
game_over_scene = GameOverScene()
menu_scene = MenuScene()
game_scene = GameScene()


if __name__ == "__main__":
   splash_scene()
