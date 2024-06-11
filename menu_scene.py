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

class menu_scene():
   # this function is the menu scene


   # image banksfor CircuitPython
   image_bank_mt_background = stage.Bank.from_bmp16("assets/mt_game_studio.bmp")




   # add text objects
   text = []
   text1 = stage.Text(
      width=29, height=12, font=None, palette=constants.RED_PALETTE,
      buffer=None
   )
   text1.move(20, 10)
   text1.text("MT Game Studios")
   text.append(text1)


   text2 = stage.Text(
      width=29, height=12, font=None, palette=constants.RED_PALETTE,
      buffer=None
   )
   text2.move(40, 110)
   text2.text("PRESS START")
   text.append(text2)




   # sets the background to image 0 in the image bank
   background = stage.Grid(
      image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
   )


# used this program to split the image into tile:
   #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
   background.tile(2, 2, 0)  # blank white
   background.tile(3, 2, 1)
   background.tile(4, 2, 2)
   background.tile(5, 2, 3)
   background.tile(6, 2, 4)
   background.tile(7, 2, 0)  # blank white


   background.tile(2, 3, 0)  # blank white
   background.tile(3, 3, 5)
   background.tile(4, 3, 6)
   background.tile(5, 3, 7)
   background.tile(6, 3, 8)
   background.tile(7, 3, 0)  # blank white


   background.tile(2, 4, 0)  # blank white
   background.tile(3, 4, 9)
   background.tile(4, 4, 10)
   background.tile(5, 4, 11)
   background.tile(6, 4, 12)
   background.tile(7, 4, 0)  # blank white


   background.tile(2, 5, 0)  # blank white
   background.tile(3, 5, 0)
   background.tile(4, 5, 13)
   background.tile(5, 5, 14)
   background.tile(6, 5, 0)
   background.tile(7, 5, 0)  # blank white


   # create a stage for the background to show up on
   # and set the frame rate to 60fps
   game = stage.Stage(ugame.display, constants.FPS)
   # set the layers, items show up in order
   game.layers = text + [background]
   # render the background and initial location of sprite list
   # most likely you will only render background once per scene
   game.render_block()


   # repeat forever, game loop
   while True:
      # get user input
      keys = ugame.buttons.get_pressed()


      # Start button selected
      if keys & ugame.K_START != 0:
         game_scene()


      # update game logic
      game.tick()  # wait until refresh rate finishes

if __name__ == "__main__":
   splash_scene()