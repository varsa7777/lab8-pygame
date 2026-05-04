import random
import pygame
from dataclasses import dataclass
from typing import List, Tuple
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MIN_SQUARE_SIZE = 20
MAX_SQUARE_SIZE = 60
SQUARE_COUNT = 20
FPS = 60

@dataclass
class Square:
    rect: pygame.Rect
    velocity: Tuple[int, int]


def initialize_pygame() -> pygame.Surface:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Moving Squares")
    return screen


def create_squares(count: int) -> List[Square]:
    squares: List[Square] = []
    for _ in range(5):
        SQUARE_SIZE = 25
        x = random.randint(0, SCREEN_WIDTH - SQUARE_SIZE)
        y = random.randint(0, SCREEN_HEIGHT - SQUARE_SIZE)
        vx = 30 / SQUARE_SIZE 
        vy = 30 / SQUARE_SIZE 
        rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
        squares.append(Square(rect=rect, velocity=(vx, vy)))
    for _ in range(10):
        SQUARE_SIZE = 10
        x = random.randint(0, SCREEN_WIDTH - SQUARE_SIZE)
        y = random.randint(0, SCREEN_HEIGHT - SQUARE_SIZE)
        vx = 30 / SQUARE_SIZE 
        vy = 30 / SQUARE_SIZE 
        rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
        squares.append(Square(rect=rect, velocity=(vx, vy)))
    for _ in range(30):
        SQUARE_SIZE = 4
        x = random.randint(0, SCREEN_WIDTH - SQUARE_SIZE)
        y = random.randint(0, SCREEN_HEIGHT - SQUARE_SIZE)
        vx = 30 / SQUARE_SIZE 
        vy = 30 / SQUARE_SIZE 
        rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
        squares.append(Square(rect=rect, velocity=(vx, vy)))
    return squares


def handle_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def update_squares(squares: List[Square]) -> None:
    for square in squares:
        # Find closest bigger square within 100 pixels
        min_dist = float('inf')
        closest = None
        for other in squares:
            if other != square and other.rect.size[0] > square.rect.size[0]:
                dx = square.rect.centerx - other.rect.centerx
                dy = square.rect.centery - other.rect.centery
                dist = math.hypot(dx, dy)
                if dist < min_dist:
                    min_dist = dist
                    closest = other
        
        # If there's a close bigger square, flee from it
        if closest and min_dist < 100:
            dx = square.rect.centerx - closest.rect.centerx
            dy = square.rect.centery - closest.rect.centery
            dist = math.hypot(dx, dy)
            if dist > 0:
                unit_dx = dx / dist
                unit_dy = dy / dist
                current_speed = math.hypot(square.velocity[0], square.velocity[1])
                square.velocity = (unit_dx * current_speed, unit_dy * current_speed)
        
        square.rect.x += square.velocity[0]
        square.rect.y += square.velocity[1]

        square.rect.x += random.randint(-1, 1)
        square.rect.y += random.randint(-1, 1)

        if square.rect.left < 0:
            square.rect.x = SCREEN_WIDTH
        
        if square.rect.right > SCREEN_WIDTH:
            square.rect.x = 0

        if square.rect.bottom < 0:
            square.rect.y = SCREEN_HEIGHT

        if square.rect.top > SCREEN_HEIGHT:
            square.rect.y = 0


def draw_squares(screen: pygame.Surface, squares: List[Square]) -> None:
    screen.fill((30, 30, 30))
    for square in squares:
        pygame.draw.rect(screen, (255, 255, 255), square.rect)
    pygame.display.flip()

def check_collision(a: Square, b:Square) -> bool:
    return a.collideRect(b)

def main() -> None:
    screen = initialize_pygame()
    squares = create_squares(SQUARE_COUNT)
    clock = pygame.time.Clock()

    running = True
    while running:
        if handle_events():
            running = False
            continue

        update_squares(squares)
        draw_squares(screen, squares)
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()