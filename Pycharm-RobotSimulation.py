from typing import Tuple

import pygame
import math
import random
from tkinter import messagebox

pygame.init()


class Animation:

    def __init__(self, image_name, w, h):
        self.x = random.randrange(0, 5)
        self.y = random.randrange(0, 5)
        self.image_name = pygame.image.load(image_name).convert()
        self.image_name = pygame.transform.scale(self.image_name, (w, h))
        self.fileName = []

    def move(self, n):
        if n == 0:  # left
            self.x = self.x - 1
        elif n == 1:  # up
            self.y = self.y - 1
        elif n == 2:  # right
            self.x = self.x + 1
        else:  # down
            self.y = self.y + 1


def draw_grids():
    for row in range(5):
        for column in range(5):
            color = BLACK
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])


#    define color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREEN = (213, 255, 179)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 100
HEIGHT = 100
# This set the margin between each cell
MARGIN = 5
WINDOW_SIZE = [530, 530]

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tom and Jerry")
grid = []
clock = pygame.time.Clock()
gameExit = False
screen.fill(LIGHT_GREEN)

T = Animation("cat.png", 100, 100)
J = Animation("mouse.png", 60, 60)
C1 = Animation("cheese.png", 60, 60)
C2 = Animation("cheese.png", 60, 60)
C3 = Animation("cheese.png", 60, 60)

while J.x == T.x and J.y == T.y:
    J.x = random.randrange(0, 5)
    J.y = random.randrange(0, 5)
while (C1.x == T.x and C1.y == T.y) or (C1.x == J.x and C1.y == J.y):
    C1.x = random.randrange(0, 5)
    C1.y = random.randrange(0, 5)
while (C2.x == T.x and C2.y == T.y) or (C1.x == T.x and C1.y == T.y) or (C2.x == C1.x and C2.y == C1.y):
    C2.x = random.randrange(0, 5)
    C2.y = random.randrange(0, 5)
while (C3.x == T.x and C3.y == T.y) or (C3.x == J.x and C3.y == J.y) or (C3.x == C1.x and C3.y == C1.y) or (
        C3.x == C2.x and C3.y == C2.y):
    C3.x = random.randrange(0, 5)
    C3.y = random.randrange(0, 5)

draw_grids()
screen.blit(T.image_name, [(MARGIN + WIDTH) * T.x + MARGIN, (MARGIN + HEIGHT) * T.y + MARGIN, WIDTH, HEIGHT])
screen.blit(J.image_name, [(MARGIN + WIDTH) * J.x + MARGIN + 20, (MARGIN + HEIGHT) * J.y + MARGIN + 20, WIDTH, HEIGHT])
screen.blit(C1.image_name,
            [(MARGIN + WIDTH) * C1.x + MARGIN + 20, (MARGIN + HEIGHT) * C1.y + MARGIN + 20, WIDTH, HEIGHT])
screen.blit(C2.image_name,
            [(MARGIN + WIDTH) * C2.x + MARGIN + 20, (MARGIN + HEIGHT) * C2.y + MARGIN + 20, WIDTH, HEIGHT])
screen.blit(C3.image_name,
            [(MARGIN + WIDTH) * C3.x + MARGIN + 20, (MARGIN + HEIGHT) * C3.y + MARGIN + 20, WIDTH, HEIGHT])
number = 0
gold_count = 0
while not gameExit:
    pygame.time.delay(300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    if T.x == J.x and T.y == J.y:
        messagebox.showinfo("Game End", "Tom wins this round")
        gameExit = True
    if gold_count == 3:
        messagebox.showinfo("Game End", "Jerry wins this round")
        gameExit = True
    J_tempx = J.x
    J_tempy = J.y
    T_tempx = T.x
    T_tempy = T.y
    if number % 2 == 0:

        if 0 < J.x < 4 and 0 < J.y < 4:
            J.move(random.randrange(0, 4))
            while J.x == T.x and J.y == T.y:
                J.x = J_tempx
                J.y = J_tempy
                J.move(random.randrange(0, 4))
        elif J.x == 0 or J.x == 4 or J.y == 0 or J.y == 4:
            if J.x == 0 and J.y == 0:
                J.move(random.randrange(2, 4))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.randrange(2, 4))
            elif J.x == 4 and J.y == 4:
                J.move(random.randrange(0, 2))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.randrange(0, 2))
            elif J.x == 4 and J.y == 0:
                J.move(random.randrange(0, 4, 3))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.randrange(0, 4, 3))
            elif J.x == 0 and J.y == 4:
                J.move(random.randrange(1, 3))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.randrange(1, 3))
            elif J.x == 0:
                value = list(range(1, 4))
                J.move(random.choice(value))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.choice(value))
            elif J.x == 4:
                value = list(range(0, 4))
                value.remove(2)
                J.move(random.choice(value))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.choice(value))
            elif J.y == 0:
                value = list(range(0, 4))
                value.remove(1)
                J.move(random.choice(value))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.choice(value))
            else:
                J.move(random.randrange(0, 3))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.randrange(0, 3))

        screen.blit(T.image_name, [(MARGIN + WIDTH) * T.x + MARGIN, (MARGIN + HEIGHT) * T.y + MARGIN, WIDTH, HEIGHT])
        screen.blit(J.image_name,
                    [(MARGIN + WIDTH) * J.x + MARGIN + 20, (MARGIN + HEIGHT) * J.y + MARGIN + 20, WIDTH, HEIGHT])
        pygame.draw.rect(screen, BLACK,
                         [(MARGIN + WIDTH) * J_tempx + MARGIN, (MARGIN + HEIGHT) * J_tempy + MARGIN, WIDTH, HEIGHT])
    if number % 2 == 1:
        if 0 < J.x < 4 and 0 < J.y < 4:
            J.move(random.randrange(0, 4))
            while J.x == T.x and J.y == T.y:
                J.x = J_tempx
                J.y = J_tempy
                J.move(random.randrange(0, 4))
        elif J.x == 0 or J.x == 4 or J.y == 0 or J.y == 4:
            if J.x == 0 and J.y == 0:
                J.move(random.randrange(2, 4))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.randrange(2, 4))
            elif J.x == 4 and J.y == 4:
                J.move(random.randrange(0, 2))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.randrange(0, 2))
            elif J.x == 4 and J.y == 0:
                J.move(random.randrange(0, 4, 3))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.randrange(0, 4, 3))
            elif J.x == 0 and J.y == 4:
                J.move(random.randrange(1, 3))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.randrange(1, 3))
            elif J.x == 0:
                value = list(range(1, 4))
                J.move(random.choice(value))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.choice(value))
            elif J.x == 4:
                value = list(range(0, 4))
                value.remove(2)
                J.move(random.choice(value))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.choice(value))
            elif J.y == 0:
                value = list(range(0, 4))
                value.remove(1)
                J.move(random.choice(value))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.choice(value))
            else:
                J.move(random.randrange(0, 3))
                while J.x == T.x and J.y == T.y:
                    J.x = J_tempx
                    J.y = J_tempy
                    J.move(random.randrange(0, 3))

        if 0 < T.x < 4 and 0 < T.y < 4:
            T.move(random.randrange(0, 4))
            while (T.x == C1.x and T.y == C1.y) or (T.x == C2.x and T.y == C2.y) or (T.x == C3.x and T.y == C3.y):
                T.x = T_tempx
                T.y = T_tempy
                T.move(random.randrange(0, 4))
        elif T.x == 0 or T.x == 4 or T.y == 0 or T.y == 4:
            if T.x == 0 and 0 == T.y:
                T.move(random.randrange(2, 4))
                while (T.x == C1.x and T.y == C1.y) or (T.x == C2.x and T.y == C2.y) or (T.x == C3.x and T.y == C3.y):
                    T.x = T_tempx
                    T.y = T_tempy
                    T.move(random.randrange(2, 4))
            elif T.x == 4 and T.y == 4:
                T.move(random.randrange(0, 2))
                while (T.x == C1.x and T.y == C1.y) or (T.x == C2.x and T.y == C2.y) or (T.x == C3.x and T.y == C3.y):
                    T.x = T_tempx
                    T.y = T_tempy
                    T.move(random.randrange(0, 2))
            elif T.x == 4 and T.y == 0:
                T.move(random.randrange(0, 4, 3))
                while (T.x == C1.x and T.y == C1.y) or (T.x == C2.x and T.y == C2.y) or (T.x == C3.x and T.y == C3.y):
                    T.x = T_tempx
                    T.y = T_tempy
                    T.move(random.randrange(0, 4, 3))

            elif T.x == 0 and T.y == 4:
                T.move(random.randrange(1, 3))
                while (T.x == C1.x and T.y == C1.y) or (T.x == C2.x and T.y == C2.y) or (T.x == C3.x and T.y == C3.y):
                    T.x = T_tempx
                    T.y = T_tempy
                    T.move(random.randrange(1, 3))
            elif T.x == 0:
                value = list(range(1, 4))
                T.move(random.choice(value))
                while (T.x == C1.x and T.y == C1.y) or (T.x == C2.x and T.y == C2.y) or (T.x == C3.x and T.y == C3.y):
                    T.x = T_tempx
                    T.y = T_tempy
                    T.move(random.choice(value))
            elif T.x == 4:
                value = list(range(0, 4))
                value.remove(2)
                T.move(random.choice(value))
                while (T.x == C1.x and T.y == C1.y) or (T.x == C2.x and T.y == C2.y) or (T.x == C3.x and T.y == C3.y):
                    T.x = T_tempx
                    T.y = T_tempy
                    T.move(random.choice(value))
            elif T.y == 0:
                value = list(range(0, 4))
                value.remove(1)
                T.move(random.choice(value))
                while (T.x == C1.x and T.y == C1.y) or (T.x == C2.x and T.y == C2.y) or (T.x == C3.x and T.y == C3.y):
                    T.x = T_tempx
                    T.y = T_tempy
                    T.move(random.choice(value))
            else:
                T.move(random.randrange(0, 3))
                while (T.x == C1.x and T.y == C1.y) or (T.x == C2.x and T.y == C2.y) or (T.x == C3.x and T.y == C3.y):
                    T.x = T_tempx
                    T.y = T_tempy
                    T.move(random.randrange(0, 3))


        screen.blit(J.image_name,
                    [(MARGIN + WIDTH) * J.x + MARGIN + 20, (MARGIN + HEIGHT) * J.y + MARGIN + 20, WIDTH, HEIGHT])
        pygame.draw.rect(screen, BLACK,
                         [(MARGIN + WIDTH) * J_tempx + MARGIN, (MARGIN + HEIGHT) * J_tempy + MARGIN, WIDTH, HEIGHT])
        screen.blit(T.image_name, [(MARGIN + WIDTH) * T.x + MARGIN, (MARGIN + HEIGHT) * T.y + MARGIN, WIDTH, HEIGHT])
        pygame.draw.rect(screen, BLACK,
                         [(MARGIN + WIDTH) * T_tempx + MARGIN, (MARGIN + HEIGHT) * T_tempy + MARGIN, WIDTH, HEIGHT])
    if (J.x == C1.x and J.y == C1.y) or (J.x == C2.x and J.y == C2.y) or (J.x == C3.x and J.y == C3.y):
        if J.x == C1.x and J.y == C1.y:
            C1.x = -1
            C1.y = -1
        elif J.x == C2.x and J.y == C2.y:
            C2.x = -1
            C2.y = -1
        elif J.x == C3.x and J.y == C3.y:
            C3.x = -1
            C3.y = -1
        gold_count += 1
    number = number + 1
    pygame.display.flip()
    print("Jerry Position %3d%3d  Tom Position %3d%3d  Cheese 1 %3d%3d  Cheese 2 %3d%3d  Cheese 3 %3d%3d" % (
    J.x, J.y, T.x, T.y, C1.x, C1.y, C2.x, C2.y, C3.x, C3.y))

pygame.quit()
quit()
