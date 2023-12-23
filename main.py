import pygame
import swarm



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Swarmer')
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the window
    width, height = 800, 600
    window = pygame.display.set_mode((width, height))

    # Set the title of the window
    pygame.display.set_caption("Swixel Swarm")

    # Define colors
    COLOR_GREEN = (0, 128, 0)
    COLOR_BACKGROUND = (0, 0, 0)

    FLOCK_SIZE = 1000

    # create test swarmer
    flock = swarm.Swarm(window, width//2, height//2, 1000, COLOR_GREEN)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # redraw the frame
        window.fill(COLOR_BACKGROUND)
        # update swarmers with current mouse pos
        m = pygame.mouse.get_pos()
        flock.draw()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
