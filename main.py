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
clock = pygame.time.Clock()

game_font = pygame.font.SysFont('Iosevka', 30)
xo_font = pygame.font.SysFont('Iosevka', 300)

def clean():
    win.fill(WHITE)
    board.clear_board()

board = Board(xo_font, RED, BLUE)
button = Button("Try again", GREEN, pos=(1070, HEIGHT / 2), font=game_font, callback=clean)
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

    board.draw(win)
    print(True)
    if not board.check_win():
        board.check_click(win, turn)
        if board.is_full():
            winner = game_font.render('No winner', True, RED)
            win.blit(winner, (1050, 300))
    else:
        winner = game_font.render(f'We have a winner', True, RED)
        win.blit(winner, (1050, 300))

    button.draw(win)
    button.check_click()

    clock.tick(20)
    pygame.display.update()

pygame.quit()
