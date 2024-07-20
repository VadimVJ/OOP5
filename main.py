# ТОРПЕДНАЯ АТАКА

# Вот пример программы на Python с использованием библиотеки Pygame для игры "ТОРПЕДНАЯ АТАКА".В
# этом примере реализована основная логика, включая движение торпедного аппарата, стрельбу
# торпедами, движение корабля и обработку столкновений.


# Вот пример кода на Python с использованием библиотеки Pygame.
# В этом коде создается игра,
# в которой корабль движется по верхней части экрана, а торпедный аппарат — по нижней.
# Игрок управляет торпедным аппаратом с помощью стрелок, а
# торпеды запускаются нажатием стрелки вверх.

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SHIP_WIDTH = 100
SHIP_HEIGHT = 50
TORPEDO_WIDTH = 10
TORPEDO_HEIGHT = 20
SHIP_SPEED = 5
TORPEDO_SPEED = 7

# Цвета
COLOR_AQUAMARINE = (127, 255, 212)
COLOR_BLACK = (0, 0, 0)

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Корабль и торпеда")

# Класс для корабля
class Ship:
    def __init__(self):
        self.rect = pygame.Rect(0, 10, SHIP_WIDTH, SHIP_HEIGHT)
        self.direction = 1  # 1 - вправо, -1 - влево

    def update(self):
        self.rect.x += self.direction * SHIP_SPEED
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.direction *= -1  # Изменение направления

# Класс для торпеды
class Torpedo:
    def __init__(self, x):
        self.rect = pygame.Rect(x, SCREEN_HEIGHT - 30, TORPEDO_WIDTH, TORPEDO_HEIGHT)

    def update(self):
        self.rect.y -= TORPEDO_SPEED

# Основная функция
def main():
    clock = pygame.time.Clock()
    ship = Ship()
    torpedoes = []
    game_over = False
    font = pygame.font.Font(None, 74)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if ship.rect.left > 0:
                        ship.rect.x -= SHIP_SPEED
                if event.key == pygame.K_RIGHT:
                    if ship.rect.right < SCREEN_WIDTH:
                        ship.rect.x += SHIP_SPEED
                if event.key == pygame.K_UP and not game_over:
                    torpedoes.append(Torpedo(ship.rect.centerx))

        if not game_over:
            ship.update()
            for torpedo in torpedoes[:]:
                torpedo.update()
                # Проверка попадания в корабль
                if torpedo.rect.colliderect(ship.rect):
                    game_over = True
                if torpedo.rect.bottom < 0:
                    torpedoes.remove(torpedo)

        # Отрисовка
        screen.fill(COLOR_AQUAMARINE)
        pygame.draw.rect(screen, COLOR_BLACK, ship.rect)

        for torpedo in torpedoes:
            pygame.draw.rect(screen, COLOR_BLACK, torpedo.rect)

        if game_over:
            text = font.render("КОРАБЛЬ ТОРПЕДИРОВАН", True, COLOR_BLACK)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
