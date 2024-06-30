from vgc.vgc import VGC
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
        if vgc.input.get_key_value(vgc.input.key1):
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # draw text
        font = pygame.font.Font(None, 36)
        text = font.render("Hello, World!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(vgc.display_size[0] // 2, vgc.display_size[1] // 2))
        screen.blit(text, text_rect)
        
        # Update the LCD
        screen = pygame.transform.rotate(screen, 90)
        screen = pygame.transform.flip(screen, True, False)
        vgc.draw(screen)
        
        # Limit to 60 frames per second
        clock.tick(60)
        
    pygame.quit()
    vgc.quit()

if __name__ == '__main__':
    main()