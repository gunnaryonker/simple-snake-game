import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 600
screen_height = 400
cell_size = 20
grid_width = screen_width // cell_size
grid_height = screen_height // cell_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(screen_width / 2, screen_height / 2)]
        self.direction = (0, 0)  # Initialize direction as a tuple
        self.color = WHITE

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        x, y = self.direction  # Unpack direction tuple here
        cur = self.get_head_position()
        new = (((cur[0] + (x * cell_size)) % screen_width), (cur[1] + (y * cell_size)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(screen_width / 2, screen_height / 2)]
        self.direction = (0, 0)

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (cell_size, cell_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    self.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.turn((1, 0))

# Fruit class
class Fruit:
    def __init__(self):
        self.position = (0, 0)
        self.color = WHITE
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width - 1) * cell_size, random.randint(0, grid_height - 1) * cell_size)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (cell_size, cell_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

# Main function
def main():
    # Initialize game objects
    snake = Snake()
    fruit = Fruit()

    clock = pygame.time.Clock()

    while True:
        screen.fill(BLACK)
        snake.handle_keys()
        snake.move()

        if snake.get_head_position() == fruit.position:
            snake.length += 1
            fruit.randomize_position()

        snake.draw(screen)
        fruit.draw(screen)
        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
