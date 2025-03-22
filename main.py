import pygame
import random

#add something new
# Settings
width = 300
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
colors = [cyan, blue, black, white, yellow, green, red, magenta]
block_size = 30

# Shapes
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

# Classes
class Piece:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = width // block_size // 2 - len(shape[0]) // 2  # Horizontal center of screen
        self.y = 0 

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]  # Rotate 90 degrees

    def get_rect(self):
        """Return the positions of all blocks making up the piece."""
        positions = []
        for i, row in enumerate(self.shape):
            for j, value in enumerate(row):
                if value:
                    positions.append((self.x + j, self.y + i))
        return positions


# Initialize pygame
pygame.init()

# Functions
def draw_piece(piece):
    """Draw the current piece on the screen."""
    for x, y in piece.get_rect():
        pygame.draw.rect(screen, piece.color, (x * block_size, y * block_size, block_size, block_size))

def check_collision(board, piece):
    """Check if the piece has collided with anything on the board."""
    for x, y in piece.get_rect():
        if x < 0 or x >= width // block_size or y >= height // block_size or board[y][x]:
            return True
    return False

def merge_piece(board, piece):
    """Merge the piece into the board."""
    for x, y in piece.get_rect():
        board[y][x] = piece.color

def clear_lines(board):
    """Clear completed lines from the board."""
    new_board = [row for row in board if any(cell == black for cell in row)]
    lines_cleared = height // block_size - len(new_board)
    new_board = [[black] * (width // block_size)] * lines_cleared + new_board
    return new_board, lines_cleared

# Create game board
board = [[black] * (width // block_size) for _ in range(height // block_size)]

# Main game loop
exit = False
clock = pygame.time.Clock()
current_piece = Piece(random.choice(shapes), random.choice(colors))
fall_time = 0

while not exit:
    screen.fill(black)
    fall_speed = 500  # Milliseconds between piece drops
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_piece.x -= 1
                if check_collision(board, current_piece):
                    current_piece.x += 1  # Revert if collision occurs
            elif event.key == pygame.K_RIGHT:
                current_piece.x += 1
                if check_collision(board, current_piece):
                    current_piece.x -= 1  # Revert if collision occurs
            elif event.key == pygame.K_DOWN:
                current_piece.y += 1
                if check_collision(board, current_piece):
                    current_piece.y -= 1  # Revert if collision occurs
            elif event.key == pygame.K_UP:
                current_piece.rotate()
                if check_collision(board, current_piece):
                    current_piece.rotate()  # Revert if collision occurs

    # Piece falling logic
    fall_time += clock.get_rawtime()
    clock.tick()

    if fall_time > fall_speed:
        current_piece.y += 1
        if check_collision(board, current_piece):
            current_piece.y -= 1
            merge_piece(board, current_piece)
            board, lines_cleared = clear_lines(board)
            current_piece = Piece(random.choice(shapes), random.choice(colors))
        fall_time = 0

    # Draw the board
    for y, row in enumerate(board):
        for x, color in enumerate(row):
            pygame.draw.rect(screen, color, (x * block_size, y * block_size, block_size, block_size))

    # Draw the current falling piece
    draw_piece(current_piece)

    pygame.display.update()

pygame.quit()
