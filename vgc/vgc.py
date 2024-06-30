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
        
    def up(self) -> bool:
        return self.config.digital_read(self.config.GPIO_KEY_UP_PIN)
    
    def down(self) -> bool:
        return self.config.digital_read(self.config.GPIO_KEY_DOWN_PIN)
    
    def left(self) -> bool:
        return self.config.digital_read(self.config.GPIO_KEY_LEFT_PIN)
    
    def right(self) -> bool:
        return self.config.digital_read(self.config.GPIO_KEY_RIGHT_PIN)
    
    def press(self) -> bool:
        return self.config.digital_read(self.config.GPIO_KEY_PRESS_PIN)
    
    def key1(self) -> bool:
        return self.config.digital_read(self.config.GPIO_KEY1_PIN)
    
    def key2(self) -> bool:
        return self.config.digital_read(self.config.GPIO_KEY2_PIN)
    
    def key3(self) -> bool:
        return self.config.digital_read(self.config.GPIO_KEY3_PIN)