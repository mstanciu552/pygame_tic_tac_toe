import pygame

class Button:
    def __init__(self, text, bg, pos, font):
        self.text = text
        self.pos = pos
        self.bg = bg
        self.replay = font.render(text, True, (0, 0, 0))

    def transform(self, pos):
        return (pos[0] + 21, pos[1] + 10)

    def draw(self, win):
        pygame.draw.rect(win, self.bg, pygame.Rect(self.pos[0], self.pos[1], 120, 60))
        win.blit(self.replay, self.transform(self.pos))
        
    def check_click(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if self.pos[0] <= mouse_x and mouse_x <= (self.pos[0] + 1):
                if self.pos[1] <= mouse_y and mouse_y <= (self.pos[1] + 1):
                    print('Pressed')

