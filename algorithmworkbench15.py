#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2021
# This program draws a circle inside a square

import pygame  # Importing the pygame library

def main():
	# This function will create a circle inside of a square

	# Initializing a surface object for the shapes to appear on (100 x 100)
	screen = pygame.display.set_mode((120, 120))
	screen.fill((255, 255, 255, 255))

	# Creating the square
	pygame.draw.rect(screen, pygame.Color((0, 0, 255)), pygame.Rect(10, 10, 100, 100), 1)

	# Creating the circle
	pygame.draw.circle(screen, pygame.Color((255, 0, 0)), (60,60), 40)

	# Displaying the circle for a brief time
	pygame.display.update()
	pygame.time.delay(10000)


if __name__ == "__main__":
    main()