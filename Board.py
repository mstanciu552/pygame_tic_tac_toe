import pygame

class Board:
    def __init__(self, font, RED, BLUE):
        self.w, self.h = pygame.display.get_surface().get_size()
        self.rect_w, self.rect_h = (300, 300)
        self.X = font.render('X', True, RED)
        self.O = font.render('O', True, BLUE)
        self.pieces = [['', '', ''], ['', '', ''], ['', '', '']]

    def normalize(self, position):
        return (position[0] * self.rect_w + self.rect_w / 4, position[1] * self.rect_h - self.rect_h / 8)

    def is_full(self):
        for row in self.pieces:
            for col in row:
                if col == '':
                    return False
        return True

    def draw(self, win):
        for x in range(3):
            for y in range(3):
                pygame.draw.rect(win, (0, 0, 0), pygame.Rect(x * self.rect_w, y * self.rect_h, self.rect_w, self.rect_h), 2)

    def check_win(self):
        def is_same_horiz(arr):
            if arr[0] == arr[1] and arr[1] == arr[2] and arr[0] != '':
                return True
            return False

        def is_same_vert(mat):
            if mat[0][0] == mat[1][0] and mat[1][0] == mat[2][0] and mat[0][0] != '':
                return True
            elif mat[0][1] == mat[1][1] and mat[1][1] == mat[2][1] and mat[0][1] != '': 
                return True
            elif mat[0][2] == mat[1][2] and mat[1][2] == mat[2][2] and mat[0][2] != '': 
                return True
            return False

        def is_same_diag(mat):
            if mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[0][0] != '':
                return True
            elif mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0] and mat[0][2] != '':
                return True
            return False
        
        if is_same_horiz(self.pieces[0]) or is_same_horiz(self.pieces[1]) or is_same_horiz(self.pieces[2]):
            return True
        if is_same_vert(self.pieces):
            return True
        if is_same_diag(self.pieces):
            return True
        return False

    def get_length(self):
        length = 0
        
        for row in self.pieces:
            for col in row:
                if col:
                    length += 1

        return length

    def get_bounds(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > 900:
            return None
        for x in range(4):
            for y in range(4):
                if x * self.rect_w <= mouse_x and mouse_x <= (x + 1) * self.rect_w:
                    if y * self.rect_h <= mouse_y and mouse_y <= (y + 1) * self.rect_h:
                        return (x, y)
        return None

            
    def check_click(self, win, turn):
        pos = self.get_bounds() if pygame.mouse.get_pressed()[0] else (-1, -1)
        piece = 'O' if turn % 2 == 1 else 'X'

        if not pos:
            return
        if not self.pieces[pos[0]][pos[1]] and pos != (-1, -1) and pos and self.get_length() != -1:
            win.blit(self.X if piece == 'X' else self.O, self.normalize(pos))
            self.pieces[pos[0]][pos[1]] = piece
    
    def clear_board(self):
        self.pieces = [['', '', ''], ['', '', ''], ['', '', '']]
