import random
import pygame
from dataclasses import dataclass
from typing import List, Tuple

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_SIZE = 40
SQUARE_COUNT = 10
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
    for _ in range(count):
        x = random.randint(0, SCREEN_WIDTH - SQUARE_SIZE)
        y = random.randint(0, SCREEN_HEIGHT - SQUARE_SIZE)
        vx = random.choice([-3, -2, -1, 1, 2, 3])
        vy = random.choice([-3, -2, -1, 1, 2, 3])
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
        square.rect.x += square.velocity[0]
        square.rect.y += square.velocity[1]

        if square.rect.left < 0 or square.rect.right > SCREEN_WIDTH:
            square.velocity = (-square.velocity[0], square.velocity[1])
            square.rect.x = max(0, min(square.rect.x, SCREEN_WIDTH - SQUARE_SIZE))

        if square.rect.top < 0 or square.rect.bottom > SCREEN_HEIGHT:
            square.velocity = (square.velocity[0], -square.velocity[1])
            square.rect.y = max(0, min(square.rect.y, SCREEN_HEIGHT - SQUARE_SIZE))


def draw_squares(screen: pygame.Surface, squares: List[Square]) -> None:
    screen.fill((30, 30, 30))
    for square in squares:
        pygame.draw.rect(screen, (255, 255, 255), square.rect)
    pygame.display.flip()


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
