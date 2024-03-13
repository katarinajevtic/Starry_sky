import random
import pygame


# Function to draw a star on the screen at the specified position
def draw_star(screen, color, pos):
    pygame.draw.circle(screen, color, pos, 1)

# Function to draw a starry night on the screen
def draw_starry_night(screen, num_stars):
    for _ in range(num_stars):
        x = random.randint(0, screen.get_width())
        y = random.randint(0, screen.get_height())
        draw_star(screen, (255, 255, 255), (x, y))

# Main function
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((0, 0, 55))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            pygame.image.save(screen, "starry_sky.png")
            print("Image saved!")

        screen.fill((0, 0, 55))
        draw_starry_night(screen, num_stars=100)  # Draw stars
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
