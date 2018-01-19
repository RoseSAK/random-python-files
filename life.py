import os, sys
import pygame
from pygame.locals import *

try:
    import numpy as np
    import pygame.surfarray as surfarray
except ImportError:
    raise ImportError("NumPy and Surfarray are required.")

if not pygame.font: 
	print('Warning, fonts disabled')
if not pygame.mixer: 
	print('Warning, sound disabled')

# Define colours

B = (0, 0, 0)
W = (255, 255, 255)

done = False

clock = pygame.time.Clock()

class PyManMain:

	def __init__(self, width=400, height=400):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
	
	def create_grid(self):
		for y in range(self.height):
			for x in range(self.width):
				rect = Rect(x*4, y*4, 4, 4)
				pygame.draw.rect(window, color, rect)

	def MainLoop(self):
		while 1: 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

class Cell:

	def __init__(self, status)
		self.status = status

	def stats(self):
		
	
	def get_status(self):

	def make_rows(grid):
		for [i, :] in grid:
			rows = [i:i+3]

	def make_columns(grid)
		for 

	def get_cell_status(cell):
	
		
	
	
if __name__ == "__main__":
	MainWindow = PyManMain()
	PyManMain.create_grid
	MainWindow.MainLoop()
	


background = np.zeros((400, 400))
surfdemo_show(allblack, 'allblack')

pygame.color

