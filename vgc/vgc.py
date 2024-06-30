import vgc.lcd as lcd
import pygame
import vgc.config as Config

class VGC:
    def __init__(self):
        self.display = lcd.LCD()
        self.display.init(lcd.SCAN_DIR_DFT)
        self.display.clear()
        self.input = Input()
        self.display_size = (self.display.width, self.display.height)
    
    def draw(self, surface: pygame.Surface):
        self.display.draw_surface(surface)
    
    def quit(self):
        self.display.clear()
        self.display.module_exit()
        
class Input:
    def __init__(self):
        config = Config.Config()
        self.up = config.digital_read(config.GPIO_KEY_UP_PIN)
        self.down = config.digital_read(config.GPIO_KEY_DOWN_PIN)
        self.left = config.digital_read(config.GPIO_KEY_LEFT_PIN)
        self.right = config.digital_read(config.GPIO_KEY_RIGHT_PIN)
        self.press = config.digital_read(config.GPIO_KEY_PRESS_PIN)
        self.key1 = config.digital_read(config.GPIO_KEY1_PIN)
        self.key2 = config.digital_read(config.GPIO_KEY2_PIN)
        self.key3 = config.digital_read(config.GPIO_KEY3_PIN)