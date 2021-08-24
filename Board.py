import pygame

class Board:
    def __init__(self, font, RED, BLUE):
        self.w, self.h = pygame.display.get_surface().get_size()
        self.rect_w, self.rect_h = (300, 300)
        self.X = font.render('X', True, RED)
        self.O = font.render('O', True, BLUE)

    def normalize(self, position):
        return (position[0] * self.rect_w + self.rect_w / 4, position[1] * self.rect_h - self.rect_h / 8)

    def draw(self, win):
        for x in range(3):
            for y in range(3):
                pygame.draw.rect(win, (0, 0, 0), pygame.Rect(x * self.rect_w, y * self.rect_h, self.rect_w, self.rect_h), 2)

    def get_bounds(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > 900:
            return None
        for x in range(3):
            for y in range(3):
                if x * self.rect_w <= mouse_x and mouse_x <= (x + 1) * self.rect_w:
                    if y * self.rect_h <= mouse_y and mouse_y <= (y + 1) * self.rect_h:
                        return (x, y)
        return None

            
    def check_click(self, turn):
        piece = 'O' if turn % 2 == 1 else 'X'
        pos = self.get_bounds() if pygame.mouse.get_pressed()[0] else (-1, -1)

        return (pos, piece)

    def render_piece(self, win, turn):
        pos, piece = self.check_click(turn)
        if not pos:
            return
        win.blit(self.X if piece == 'X' else self.O, self.normalize(pos))
