import pygame
import random
#settings
width = 300
height= 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")
#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
colors = [cyan, blue, black, white,yellow, green, red, magenta]
block_size = 30
shapes = [
    [[1, 1, 1],
     [0, 1, 0]],  # T-shape

    [[1, 1, 0],
     [0, 1, 1]],  # S-shape

    [[0, 1, 1],
     [1, 1, 0]],  # Z-shape

    [[1, 1],
     [1, 1]],  # O-shape

    [[0, 1, 0],
     [1, 1, 1]],  # T-shape rotated

    [[1, 0, 0],
     [1, 1, 1]],  # L-shape
    
    [[0, 0, 1],
     [1, 1, 1]]   # J-shape
]
#classes
 class Piece:
    def __init__(self, shape, color):
         self.shape = shape
         self.color = color
         self.x = width // block_size // 2 - len(shape[0]) // 2  # Horizontal center of screen
         self.y = 0 
    def rotate









































exit = False

while not exit:
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            exit= True
    pygame.display.update()