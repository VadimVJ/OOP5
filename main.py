# Игра "ТОРПЕДНАЯ АТАКА", управление: стрелки вправо-влево, стрельба стрелка вверх.

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
SHIP_WIDTH, SHIP_HEIGHT = 100, 50  # размеры корабля
TORPEDO_WIDTH, TORPEDO_HEIGHT = 10, 30  # размеры торпеды
TorpedoLauncher_COLOR = (0, 0, 0)
SHIP_COLOR = (0, 0, 0)
TORPEDO_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (0, 139, 139)  # темно-аквамариновый

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Торпедный аппарат")

# Класс для торпедного аппарата
class TorpedoLauncher:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.speed = 10

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < WIDTH - 50:  # 50 - ширина аппарата
            self.x += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, TorpedoLauncher_COLOR, (self.x, self.y, 50, 20))

# Класс для торпеды
class Torpedo:
    def __init__(self, x):
        self.x = x
        self.y = HEIGHT - 50
        self.speed = 15

    def move(self):
        self.y -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, TORPEDO_COLOR, (self.x, self.y, TORPEDO_WIDTH, TORPEDO_HEIGHT))

# Главная функция игры
def main():
    clock = pygame.time.Clock()
    launcher = TorpedoLauncher()
    torpedoes = []
    ship_x = 0
    ship_direction = 1  # 1 - вправо, -1 - влево
    ship_hit = False
    font = pygame.font.Font(None, 74)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    launcher.move("left")
                if event.key == pygame.K_RIGHT:
                    launcher.move("right")
                if event.key == pygame.K_UP:
                    torpedoes.append(Torpedo(launcher.x + 20))  # стрельба из центра аппарата

        # Движение корабля
        if not ship_hit:
            ship_x += ship_direction * 5
            if ship_x > WIDTH - SHIP_WIDTH or ship_x < 0:
                ship_direction *= -1

        # Обновление и движение торпед
        for torpedo in torpedoes[:]:
            torpedo.move()
            if torpedo.y < 0:  # Удаление торпед, вышедших за экран
                torpedoes.remove(torpedo)

            # Проверка на попадание в корабль
            if not ship_hit and (ship_x < torpedo.x < ship_x + SHIP_WIDTH) and (0 < torpedo.y < SHIP_HEIGHT):
                ship_hit = True

        # Рендеринг
        screen.fill(BACKGROUND_COLOR)
        launcher.draw(screen)
        pygame.draw.rect(screen, SHIP_COLOR, (ship_x, 0, SHIP_WIDTH, SHIP_HEIGHT))

        for torpedo in torpedoes:
            torpedo.draw(screen)

        if ship_hit:
            text = font.render("КОРАБЛЬ ТОРПЕДИРОВАН", True, (255, 0, 0))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()