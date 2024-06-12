#!/usr/bin/env python3


# Created by: Ava V and Kaitlyn I
# Created on: Mar 2023
# This program is the "space alien" game on pybadge

import stage
import random
import time
import supervisor


import constants

class game_scene():
   # this function is the main game game_scene

   alien_count = 0
   # for score
   score = 0


   score_text = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
   score_text.clear()
   score_text.cursor(0,0)
   score_text.move(1,1)
   score_text.text("Score: {0}".format(score))


   class show_aliens():
       this function takes an alien from off screen and moves it on screen
      or alien_number in range(len(aliens)):
        if aliens[alien_number].x < 0:
              aliens[alien_number].move(
                 random.randint(
                    0 + constants.SPRITE_SIZE,
                    constants.SCREEN_X - constants.SPRITE_SIZE,
                 ),
                    constants.OFF_TOP_SCREEN,
              )
              break


   # image banks for CircuitPython
   image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
   image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")


   # buttons that you want to keep state information on
   a_button = constants.button_state["button_up"]
   b_button = constants.button_state["button_up"]
   state_button = constants.button_state["button_up"]
   select_button = constants.button_state["button_up"]




   # gt sound ready
   pewsound = open("pew.wav", "rb")
   boom_sound = open("boom.wav", "rb")
   crash_sound = open("crash.wav", "rb")
   sound = ugame.audio
   sound.stop()
   sound.mute(False)
   # set the background to image 0 in the image bank
   # and the size (10x8 tiles for size 16x16)
   background = stage.Grid(image_bank_background, 10, 8)


   for x_location in range(constants.SCREEN_GRID_X):
      for y_location in range(constants.SCREEN_GRID_Y):
         tile_picked = random.randint(1, 3)
         background.tile(x_location, y_location, tile_picked)



   # a sprite that will be updated every frame
   ship = stage.Sprite(
      image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
   )

   alien = stage.Sprite(
      image_bank_sprites,
      9,
      int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
      16,
   )

class xy_location():

   # create list of lasers for when we shoot
   aliens = []
   for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
      a_single_alien = stage.Sprite(
         image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
      )
      aliens.append(a_single_alien)
   # place 1 alien on the screen
   show_aliens()

   # create list of lasers for when we shoot
   lasers = []
   for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
      a_single_laser = stage.Sprite(
         image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
      )
      lasers.append(a_single_laser)


   # create a stage for the background to show up on
   # and set the frame rate to 60fps
   game = stage.Stage(ugame.display, 60)
   # set the layers of all sprites, items show up in order
   game.layers = [score_text] + aliens + lasers + [ship] + [alien] + [background]


   # render all sprites
   # most likely you will only render the background once per game scene
   game.render_block()


   # repeat forever, game loop
   while True:
      # get user input
      keys = ugame.buttons.get_pressed()


      # A button to fire
      if keys & ugame.K_O != 0:
         if a_button == constants.button_state["button_up"]:
               a_button = constants.button_state["button_just_pressed"]
         elif a_button == constants.button_state["button_just_pressed"]:
               a_button = constants.button_state["button_still_pressed"]
      else:
         if a_button == constants.button_state["button_still_pressed"]:
               a_button = constants.button_state["button_released"]
         else:
               a_button = constants.button_state["button_up"]


      if keys & ugame.K_RIGHT != 0:
         if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
               ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
         else:
               ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)


      if keys & ugame.K_LEFT != 0:
         if ship.x > 0:
               ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
         else:
               ship.move(0, ship.y)


      # update game logic
      # play sound if A was just button_just_pressed
      if a_button == constants.button_state["button_just_pressed"]:
         # fire a laser, if we have enough power (have not used up all the lasers)
         for laser_number in range(len(lasers)):
               if lasers[laser_number].x < 0:
                  lasers[laser_number].move(ship.x, ship.y)
                  sound.play(pew_sound)
                  break
      # each frame move the lasers, that have been fired up
      for laser_number in range(len(lasers)):
         if lasers[laser_number].x > 0:
               lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
               if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                  lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

class alien_location(): # NEW
      # each frame move the aliens down, that are on screen
      for alien_number in range(len(aliens)):
         if aliens[alien_number].x > 0:
               aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
               if aliens[alien_number].y > constants.SCREEN_Y:
                  aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                  show_aliens()
                  score -= 1
                  if score < 0:
                     score = 0
                  score_text.clear()
                  score_text.cursor(0,0)
                  score_text.move(1,1)
                  score_text.text("Score: {0}".format(score))

class laser_location(): # NEW
      # each frame check is any of the lasers are touching any of the aliens
      for laser_number in range(len(lasers)):
         if lasers[laser_number].x > 0:
               for alien_number in range(len(aliens)):
                  if aliens[alien_number].x > 0:
                     if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                       lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                       aliens[alien_number].x + 1, aliens[alien_number].y,
                                       aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                           # you hit an alien
                           aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                           lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                           #add 1 to the score
                           score += 1
                           score_text.clear()
                           score_text.cursor(0,0)
                           score_text.move(1,1)
                           score_text.text("Score: {0}".format(score))
                           sound.stop()
                           sound.play(boom_sound)
                           show_aliens()
                           show_aliens()
                           alien_count = alien_count + 1
      # each frame check if any aliens are touching the space ship
      for alien_number in range(len(aliens)):
         if aliens[alien_number].x > 0:
               if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                              aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                              ship.x, ship.y,
                              ship.x + 15, ship.y + 15):
                  # alien hit the ship
                  sound.stop()
                  sound.play(crash_sound)
                  time.sleep(3.0)
                  game_over_scene(score)




      # redraw Sprites
      game.render_sprites(aliens + lasers + [ship])
      game.tick()

