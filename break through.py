import pygame
import random

# 초기화
pygame.init()

# 화면 크기
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# 색상
WHITE = (255, 255, 255)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 40, paddle_width, paddle_height)

# 공 설정
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 10, 10)
ball_dx = 4 * random.choice([-1, 1])
ball_dy = -4

# 블록 설정
blocks = []
block_rows = 5
block_cols = 10
block_width = WIDTH // block_cols
block_height = 20

for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(col * block_width, row * block_height + 40, block_width - 5, block_height - 5)
        blocks.append(block)

# 게임 루프
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)  # FPS
    screen.fill(BLACK)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 7
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += 7

    # 공 이동
    ball.x += ball_dx
    ball.y += ball_dy

    # 벽 충돌
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx *= -1
    if ball.top <= 0:
        ball_dy *= -1

    # 바닥 닿음 → 리셋
    if ball.bottom >= HEIGHT:
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_dx *= random.choice([-1, 1])
        ball_dy = -4

    # 패들과 충돌
    if ball.colliderect(paddle):
        ball_dy *= -1

    # 블록과 충돌
    hit_block = None
    for block in blocks:
        if ball.colliderect(block):
            hit_block = block
            break
    if hit_block:
        blocks.remove(hit_block)
        ball_dy *= -1

    # 객체 그리기
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    pygame.display.flip()

pygame.quit()
