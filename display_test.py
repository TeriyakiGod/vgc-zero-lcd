from lcd import LCD, SCAN_DIR_DFT
import pygame

def main():
    lcd = LCD()
    lcd.LCD_Init(SCAN_DIR_DFT)
    lcd.LCD_Clear()

    pygame.init()
    
    screen_size = (128, 128)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    
    # Define the rectangle starting position and size
    rect_x = 0
    rect_y = 0
    rect_width = 40
    rect_height = 40
    
    # Define the speed of the rectangle
    rect_change_x = 2
    rect_change_y = 2
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Draw the rectangle
        pygame.draw.rect(screen, (255, 0, 0), [rect_x, rect_y, rect_width, rect_height])
        
        # Move the rectangle
        rect_x += rect_change_x
        rect_y += rect_change_y
        
        # Bounce the rectangle if it hits the boundary
        if rect_x > screen_size[0] - rect_width or rect_x < 0:
            rect_change_x = rect_change_x * -1
        if rect_y > screen_size[1] - rect_height or rect_y < 0:
            rect_change_y = rect_change_y * -1
        
        # Update the LCD with the Pygame surface
        lcd.LCD_DrawPygameSurface(screen)
        
        # Limit to 60 frames per second
        clock.tick(60)
        
    pygame.quit()

if __name__ == '__main__':
    main()