from vgc.vgc import VGC
import pygame

# Simple game running on the VGC
def main():
    vgc = VGC()
    pygame.init()
    
    screen = pygame.display.set_mode(vgc.display_size)
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Game logic
        test(vgc, screen)
        
        # Update the LCD
        vgc.draw(screen)
        
        # Limit to 60 frames per second
        clock.tick(60)
        
    pygame.quit()
    vgc.quit()

if __name__ == '__main__':
    main()
    
def test(vgc, screen):
    if vgc.input.up == 0: 
            pygame.draw.polygon(screen, (255, 255, 255), [(20, 20), (30, 2), (40, 20)], 0)      
    else:
        pygame.draw.polygon(screen, (255, 255, 255), [(20, 20), (30, 2), (40, 20)], 1)
        print ("Up" )
    if vgc.input.down == 0: 
            pygame.draw.polygon(screen, (255, 255, 255), [(20, 60), (30, 80), (40, 60)], 0)
    else:
        pygame.draw.polygon(screen, (255, 255, 255), [(20, 60), (30, 80), (40, 60)], 1)
        print ("Down")
    if vgc.input.left == 0: 
            pygame.draw.polygon(screen, (255, 255, 255), [(20, 100), (2, 90), (20, 80)], 0)
    else:
        pygame.draw.polygon(screen, (255, 255, 255), [(20, 100), (2, 90), (20, 80)], 1)
        print ("Left")
    if vgc.input.right == 0: 
            pygame.draw.polygon(screen, (255, 255, 255), [(40, 100), (60, 90), (40, 80)], 0)
    else:
        pygame.draw.polygon(screen, (255, 255, 255), [(40, 100), (60, 90), (40, 80)], 1)
        print ("Right")
    if vgc.input.press == 0: 
            pygame.draw.circle(screen, (255, 255, 255), (30, 40), 10, 0)
    else:
        pygame.draw.circle(screen, (255, 255, 255), (30, 40), 10, 1)
        print ("Press")
    if vgc.input.key1 == 0: 
            pygame.draw.circle(screen, (255, 255, 255), (30, 80), 10, 0)
    else:
        pygame.draw.circle(screen, (255, 255, 255), (30, 80), 10, 1)
        print ("Key1")
    if vgc.input.key2 == 0: 
            pygame.draw.circle(screen, (255, 255, 255), (30, 120), 10, 0)
    else:
        pygame.draw.circle(screen, (255, 255, 255), (30, 120), 10, 1)
        print ("Key2")
    if vgc.input.key3 == 0: 
            pygame.draw.circle(screen, (255, 255, 255), (30, 160), 10, 0)
    else:
        pygame.draw.circle(screen, (255, 255, 255), (30, 160), 10, 1)
        print ("Key3")
        