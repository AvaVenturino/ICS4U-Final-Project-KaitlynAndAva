#!/usr/bin/env python3

# Created by: Ava V and Kaitlyn I
# Created on: Mar 2023
# This program is the "space alien" game on pybadge

import stage
import random
import time
import supervisor
import constants

class SpaceAlienGame:
    def __init__(self):
        # Initialize game properties if needed
        pass

    def game_over_scene(self, final_score):
        # This function is the game over scene

        # Turn off sound from the last scene
        sound = ugame.audio
        sound.stop()

        # Image banks for CircuitPython
        image_bank_2 = stage.Bank.from_bmp16("assets/mt_game_studio.bmp")

        # Set the background to image 0 in the image bank
        background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

        # Add text objects
        text = []
        text1 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
        text1.move(22, 20)
        text1.text("Final Score: {:0>2d}".format(final_score))
        text.append(text1)

        text2 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
        text2.move(43, 60)
        text2.text("GAME OVER")
        text.append(text2)

        text3 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
        text3.move(32, 110)
        text3.text("PRESS SELECT")
        text.append(text3)

        # Create a stage for the background to show up on and set the frame rate to 60fps
        game = stage.Stage(ugame.display, constants.FPS)
        # Set the layers, items show up in order
        game.layers = text + [background]
        # Render the background and initial location of sprite list
        # Most likely you will only render the background once per scene
        game.render_block()

        # Repeat forever, game loop
        while True:
            # Get user input
            keys = ugame.buttons.get_pressed()

            # Start button selected
            if keys & ugame.K_SELECT != 0:
                supervisor.reload()

            # Update game logic
            game.tick()

    def splash_scene(self):
        # Placeholder for the splash scene method
        pass

if __name__ == "__main__":
    game = SpaceAlienGame()
    game.splash_scene()
