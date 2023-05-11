import pygame

from graphics_utils import *

class Animator():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # initialize game window
        pygame.init()
        self.window = pygame.display.set_mode((self.width+1, self.height+1))
        self.window.fill(BACKGROUND_COLOR)
        pygame.display.set_caption("Graph Search")
        pygame.display.flip()

        self.font = pygame.font.SysFont('monospace', 16, bold=True)

    
    # basic operations
    def quit(self):
        pygame.quit()

    def flip(self):
        pygame.display.flip()


    # basic draw functions
    def draw_point(self, point, color, size=2, width=0, flip=True):
        pygame.draw.circle(self.window, color, (point.x, point.y), size, width)
        if flip:
            pygame.display.flip()
    
    def draw_line(self, p1, p2, color, width=2, flip=True):
        pygame.draw.line(self.window, color, [p1.x, p1.y], [p2.x, p2.y], width=width)
        if flip:
            pygame.display.flip()

    def draw_edge(self, edge, color, width=2, flip=True):
        pygame.draw.line(self.window, color, [edge.x1, edge.y1], [edge.x2, edge.y2], width=width)
        if flip:
            pygame.display.flip()

    def draw_rect(self, rect_obj, color, flip=True):
        pygame.draw.rect(self.window, color, rect_obj)
        if flip:
            pygame.display.flip()

    def draw_text(self, text, position, color=GRAPH_COLOR, flip=True):
        textObj = self.font.render(str(text), 1, color)
        self.window.blit(textObj, position)
        if flip:
            pygame.display.flip()

    def draw_vertex_value(self, vert, off=[0,0], color=BAND_COLOR, flip=True):
        textObj = self.font.render(str(vert.z), 1, color)
        self.window.blit(textObj, [vert.x+off[0], vert.y+off[1]])
        if flip:
            pygame.display.flip()


    # more complex draw functions
    def reset_screen(self, graph):
        self.window.fill(BACKGROUND_COLOR)
        graph.display()