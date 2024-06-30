from vgc import VGC
import pygame

# Simple game running on the VGC
def main():
    vgc = VGC()
    pygame.init()
    
    screen = pygame.display.set_mode(vgc.display_size)
    pygame.display.set_caption('Game')
    clock = pygame.time.Clock()
    running = True
    
    while running:
        if vgc.input.key1():
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # draw text
        font = pygame.font.Font(None, 24)
        text = font.render("hello world", False, (255, 255, 255))
        text_rect = text.get_rect(topleft=(0, 0))
        screen.blit(text, text_rect)
        
        # Update the LCD
        screen = pygame.transform.rotate(screen, 90)
        screen = pygame.transform.flip(screen, False, True)
        vgc.draw(screen)
        
        # Limit to 60 frames per second
        clock.tick(60)
        
    pygame.quit()
    vgc.quit()

if __name__ == '__main__':
    main()