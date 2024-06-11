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

class splash_scene():
   # this function is the menu scene


   # get sound ready
   coin_sound = open("coin.wav", "rb")
   sound = ugame.audio
   sound.stop()
   sound.mute(False)
   sound.play(coin_sound)


   # image banksfor CircuitPython
   image_bank_mt_background = stage.Bank.from_bmp16("assets/mt_game_studio.bmp")


   # sets the background to image 0 in the image bank
   background = stage.Grid(
      image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
   )


   # create a stage for the background to show up on
   # and set the frame rate to 60fps
   game = stage.Stage(ugame.display, constants.FPS)
   # set the layers, items show up in order
   game.layers = [background]
   # render the background and initial location of sprite list
   # most likely you will only render background once per scene
   game.render_block()




   # repeat forever, game loop
   while True:
      # Wait for 2 seconds
      time.sleep(2.0)
      menu_scene()