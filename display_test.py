from lcd import LCD, SCAN_DIR_DFT
import pygame

def main():
    lcd = LCD()
    lcd.LCD_Init(SCAN_DIR_DFT)
    lcd.LCD_Clear()

    pygame.init()
    
    screen_size = (128,128)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 0, 0))
        
        lcd.LCD_DrawPygameSurface(screen)
        
        clock.tick(60)
        
    pygame.quit()

if __name__ == '__main__':
    main()