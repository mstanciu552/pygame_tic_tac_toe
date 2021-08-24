import pygame
from pygame.constants import KEYDOWN, K_ESCAPE, MOUSEBUTTONUP, QUIT

from Board import Board
from Button import Button

WIDTH, HEIGHT = 1400, 900

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
win = pygame.display.set_mode([WIDTH, HEIGHT])

game_font = pygame.font.SysFont('Iosevka', 30)
xo_font = pygame.font.SysFont('Iosevka', 300)

board = Board(xo_font, RED, BLUE)
button = Button("Start", GREEN, (1070, HEIGHT / 2 + 100), game_font)
turn = 0

win.fill(WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == MOUSEBUTTONUP:
            turn += 1 # if X or O placed change turn

    move = 'X' if turn % 2 == 0 else 'O'
    moving = game_font.render(f'Moving => {move}', True, RED)
    
    win.blit(moving, (1050, HEIGHT / 2))
    
    board.draw(win)
    board.render_piece(win, turn)

    button.draw(win)

    pygame.display.update()


pygame.quit()
