import lcd
import pygame

def main():
    LCD = lcd.LCD()
    Lcd_ScanDir = lcd.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    pygame.init()
    
    screen_size = (LCD.width, LCD.height)
    screen = pygame.display.set_mode(screen_size)
    
    clock = pygame.time.Clock()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 0, 0))
        
        pygame.display.flip()
        LCD.draw_surface(screen)
        
        clock.tick(60)
        
    pygame.quit()

if __name__ == '__main__':
    main()