#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2021
# This program draws a circle with a radius of 75 pixels

import pygame  # Importing the pygame library

def main():
	# This function will create a circle with a radius of 75 pixels

	# Initializing a surface object for the shapes to appear on (100 x 100)
	screen = pygame.display.set_mode((150, 150))
	screen.fill((255, 255, 255, 255))

	# Creating the circle
	pygame.draw.circle(screen, pygame.Color(0, 0, 0), (75, 75), 75)

	# Displaying the circle for a brief time
	pygame.display.update()
	pygame.time.delay(10000)


if __name__ == "__main__":
    main()