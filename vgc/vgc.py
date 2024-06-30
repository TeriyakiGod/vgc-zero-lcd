import vgc.lcd as lcd
import pygame

class VGC:
    def __init__(self):
        self.display = lcd.LCD()
        self.display.init(lcd.SCAN_DIR_DFT)
        self.display.clear()
        self.input = Input(self.display)
        self.display_size = (self.display.width, self.display.height)
    
    def draw(self, surface: pygame.Surface):
        self.display.draw_surface(surface)
    
    def quit(self):
        self.display.clear()
        self.display.module_exit()
        
class Input:
    def __init__(self, display: lcd.LCD):
        self.up = display.digital_read(display.GPIO_KEY_UP_PIN)
        self.down = display.digital_read(display.GPIO_KEY_DOWN_PIN)
        self.left = display.digital_read(display.GPIO_KEY_LEFT_PIN)
        self.right = display.digital_read(display.GPIO_KEY_RIGHT_PIN)
        self.press = display.digital_read(display.GPIO_KEY_PRESS_PIN)
        self.key1 = display.digital_read(display.GPIO_KEY1_PIN)
        self.key2 = display.digital_read(display.GPIO_KEY2_PIN)
        self.key3 = display.digital_read(display.GPIO_KEY3_PIN)
        