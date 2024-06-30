import vgc.lcd as lcd
import pygame
import vgc.config as Config

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
    def __init__(self, config: lcd.LCD):
        self.config = config
        self.up = self.config.GPIO_KEY_UP_PIN
        self.down = self.config.GPIO_KEY_DOWN_PIN
        self.left = self.config.GPIO_KEY_LEFT_PIN
        self.right = self.config.GPIO_KEY_RIGHT_PIN
        self.press = self.config.GPIO_KEY_PRESS_PIN
        self.key1 = self.config.GPIO_KEY1_PIN
        self.key2 = self.config.GPIO_KEY2_PIN
        self.key3 = self.config.GPIO_KEY3_PIN
        
    def get_key_value(self, key) -> bool:
        return bool(self.config.digital_read(key))