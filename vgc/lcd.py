from vgc.config import Config
import time
import numpy as np
import pygame


LCD_WIDTH  = 128  #LCD width
LCD_HEIGHT = 128 #LCD height
LCD_X = 2
LCD_Y = 1

LCD_X_MAXPIXEL = 132  #LCD width maximum memory 
LCD_Y_MAXPIXEL = 162  #LCD height maximum memory

#scanning method
L2R_U2D = 1
L2R_D2U = 2
R2L_U2D = 3
R2L_D2U = 4
U2D_L2R = 5
U2D_R2L = 6
D2U_L2R = 7
D2U_R2L = 8
SCAN_DIR_DFT = U2D_R2L


class LCD(Config):

	width = LCD_WIDTH
	height = LCD_HEIGHT
	LCD_Scan_Dir = SCAN_DIR_DFT
	LCD_X_Adjust = LCD_X
	LCD_Y_Adjust = LCD_Y

	"""    Hardware reset     """
	def reset(self):
		self.digital_write(self.GPIO_RST_PIN,True)
		time.sleep(0.01)
		self.digital_write(self.GPIO_RST_PIN,False)
		time.sleep(0.01)
		self.digital_write(self.GPIO_RST_PIN,True)
		time.sleep(0.01)

	"""    Write register address and data     """
	def write_register(self, Reg):
		self.digital_write(self.GPIO_DC_PIN, False)
		self.spi_writebyte([Reg])

	def write_8bit_data(self, Data):
		self.digital_write(self.GPIO_DC_PIN, True)
		self.spi_writebyte([Data])

	def write_16bit_data(self, Data, DataLen):
		self.digital_write(self.GPIO_DC_PIN, True)
		for i in range(0, DataLen):
			self.spi_writebyte([Data >> 8])
			self.spi_writebyte([Data & 0xff])
		
	"""    Common register initialization    """
	def init_registers(self):
		#ST7735R Frame Rate
		self.write_register(0xB1)
		self.write_8bit_data(0x01)
		self.write_8bit_data(0x2C)
		self.write_8bit_data(0x2D)

		self.write_register(0xB2)
		self.write_8bit_data(0x01)
		self.write_8bit_data(0x2C)
		self.write_8bit_data(0x2D)

		self.write_register(0xB3)
		self.write_8bit_data(0x01)
		self.write_8bit_data(0x2C)
		self.write_8bit_data(0x2D)
		self.write_8bit_data(0x01)
		self.write_8bit_data(0x2C)
		self.write_8bit_data(0x2D)
		
		#Column inversion 
		self.write_register(0xB4)
		self.write_8bit_data(0x07)
		
		#ST7735R Power Sequence
		self.write_register(0xC0)
		self.write_8bit_data(0xA2)
		self.write_8bit_data(0x02)
		self.write_8bit_data(0x84)
		self.write_register(0xC1)
		self.write_8bit_data(0xC5)

		self.write_register(0xC2)
		self.write_8bit_data(0x0A)
		self.write_8bit_data(0x00)

		self.write_register(0xC3)
		self.write_8bit_data(0x8A)
		self.write_8bit_data(0x2A)
		self.write_register(0xC4)
		self.write_8bit_data(0x8A)
		self.write_8bit_data(0xEE)
		
		self.write_register(0xC5)#VCOM 
		self.write_8bit_data(0x0E)
		
		#ST7735R Gamma Sequence
		self.write_register(0xe0)
		self.write_8bit_data(0x0f)
		self.write_8bit_data(0x1a)
		self.write_8bit_data(0x0f)
		self.write_8bit_data(0x18)
		self.write_8bit_data(0x2f)
		self.write_8bit_data(0x28)
		self.write_8bit_data(0x20)
		self.write_8bit_data(0x22)
		self.write_8bit_data(0x1f)
		self.write_8bit_data(0x1b)
		self.write_8bit_data(0x23)
		self.write_8bit_data(0x37)
		self.write_8bit_data(0x00)
		self.write_8bit_data(0x07)
		self.write_8bit_data(0x02)
		self.write_8bit_data(0x10)

		self.write_register(0xe1)
		self.write_8bit_data(0x0f)
		self.write_8bit_data(0x1b)
		self.write_8bit_data(0x0f)
		self.write_8bit_data(0x17)
		self.write_8bit_data(0x33)
		self.write_8bit_data(0x2c)
		self.write_8bit_data(0x29)
		self.write_8bit_data(0x2e)
		self.write_8bit_data(0x30)
		self.write_8bit_data(0x30)
		self.write_8bit_data(0x39)
		self.write_8bit_data(0x3f)
		self.write_8bit_data(0x00)
		self.write_8bit_data(0x07)
		self.write_8bit_data(0x03)
		self.write_8bit_data(0x10) 
		
		#Enable test command
		self.write_register(0xF0)
		self.write_8bit_data(0x01)
		
		#Disable ram power save mode
		self.write_register(0xF6)
		self.write_8bit_data(0x00)
		
		#65k mode
		self.write_register(0x3A)
		self.write_8bit_data(0x05)

	#********************************************************************************
	#function:	Set the display scan and color transfer modes
	#parameter: 
	#		Scan_dir   :   Scan direction
	#		Colorchose :   RGB or GBR color format
	#********************************************************************************
	def set_scan_direction(self, Scan_dir):
		#Get the screen scan direction
		self.LCD_Scan_Dir = Scan_dir
		
		#Get GRAM and LCD width and height
		if (Scan_dir == L2R_U2D) or (Scan_dir == L2R_D2U) or (Scan_dir == R2L_U2D) or (Scan_dir == R2L_D2U) :
			self.width	= LCD_HEIGHT 
			self.height 	= LCD_WIDTH 
			if Scan_dir == L2R_U2D:
				MemoryAccessReg_Data = 0X00 | 0x00
			elif Scan_dir == L2R_D2U:
				MemoryAccessReg_Data = 0X00 | 0x80
			elif Scan_dir == R2L_U2D:
				MemoryAccessReg_Data = 0x40 | 0x00
			else:		#R2L_D2U:
				MemoryAccessReg_Data = 0x40 | 0x80
		else:
			self.width	= LCD_WIDTH 
			self.height 	= LCD_HEIGHT 
			if Scan_dir == U2D_L2R:
				MemoryAccessReg_Data = 0X00 | 0x00 | 0x20
			elif Scan_dir == U2D_R2L:
				MemoryAccessReg_Data = 0X00 | 0x40 | 0x20
			elif Scan_dir == D2U_L2R:
				MemoryAccessReg_Data = 0x80 | 0x00 | 0x20
			else:		#R2L_D2U
				MemoryAccessReg_Data = 0x40 | 0x80 | 0x20
		
		#please set (MemoryAccessReg_Data & 0x10) != 1
		if (MemoryAccessReg_Data & 0x10) != 1:
			self.LCD_X_Adjust = LCD_Y
			self.LCD_Y_Adjust = LCD_X
		else:
			self.LCD_X_Adjust = LCD_X
			self.LCD_Y_Adjust = LCD_Y
		
		# Set the read / write scan direction of the frame memory
		self.write_register(0x36)		#MX, MY, RGB mode 
		self.write_8bit_data( MemoryAccessReg_Data | 0x08)	#0x08 set RGB


	#/********************************************************************************
	#function:	
	#			initialization
	#********************************************************************************/
	def init(self, Lcd_ScanDir):
		if (self.module_init() != 0):
			return -1
		
		#Turn on the backlight
		self.bl_DutyCycle(100)
		
		#Hardware reset
		self.reset()
		
		#Set the initialization register
		self.init_registers()
		
		#Set the display scan and color transfer modes	
		self.set_scan_direction(Lcd_ScanDir)
		self.delay_ms(200)
		
		#sleep out
		self.write_register(0x11)
		self.delay_ms(120)
		
		#Turn on the LCD display
		self.write_register(0x29)
		
	#/********************************************************************************
	#function:	Sets the start position and size of the display area
	#parameter: 
	#	Xstart 	:   X direction Start coordinates
	#	Ystart  :   Y direction Start coordinates
	#	Xend    :   X direction end coordinates
	#	Yend    :   Y direction end coordinates
	#********************************************************************************/
	def set_display_area_position_size(self, Xstart, Ystart, Xend, Yend):
		#set the X coordinates
		self.write_register(0x2A)
		self.write_8bit_data(0x00)
		self.write_8bit_data((Xstart & 0xff) + self.LCD_X_Adjust)
		self.write_8bit_data(0x00)
		self.write_8bit_data(((Xend - 1) & 0xff) + self.LCD_X_Adjust)

		#set the Y coordinates
		self.write_register (0x2B)
		self.write_8bit_data(0x00)
		self.write_8bit_data((Ystart & 0xff) + self.LCD_Y_Adjust)
		self.write_8bit_data(0x00)
		self.write_8bit_data(((Yend - 1) & 0xff )+ self.LCD_Y_Adjust)

		self.write_register(0x2C)

	def clear(self):
		#hello
		_buffer = [0xff]*(self.width * self.height * 2)
		self.set_display_area_position_size(0, 0, self.width, self.height)
		self.digital_write(self.GPIO_DC_PIN, True)
		for i in range(0,len(_buffer),4096):
			self.spi_writebyte(_buffer[i:i+4096])

	def draw_pil_image(self,Image,Xstart,Ystart):
		if (Image == None):
			return
		imwidth, imheight = Image.size
		if imwidth != self.width or imheight != self.height:
			raise ValueError('Image must be same dimensions as display \
				({0}x{1}).' .format(self.width, self.height))
		img = np.asarray(Image)
		pix = np.zeros((self.width,self.height,2), dtype = np.uint8)
		pix[...,[0]] = np.add(np.bitwise_and(img[...,[0]],0xF8),np.right_shift(img[...,[1]],5))
		pix[...,[1]] = np.add(np.bitwise_and(np.left_shift(img[...,[1]],3),0xE0),np.right_shift(img[...,[2]],3))
		pix = pix.flatten().tolist()
		self.set_display_area_position_size(0, 0, self.width , self.height)
		self.digital_write(self.GPIO_DC_PIN, True)
		for i in range(0,len(pix),4096):
			self.spi_writebyte(pix[i:i+4096])
   
	def draw_surface(self, surface: pygame.Surface):
		"""
		Draws a pygame surface onto the LCD screen.

		Parameters:
		- surface: pygame.Surface object to be drawn. It must have the same dimensions as LCD_WIDTH x LCD_HEIGHT.
		"""
		if surface.get_width() != self.width or surface.get_height() != self.height:
			raise ValueError('Surface dimensions must match LCD dimensions ({0}x{1}).'.format(self.width, self.height))
		
		# Convert pygame surface to numpy array
		img = pygame.surfarray.array3d(surface)
		
		# Convert RGB888 format to RGB565 format suitable for LCD
		pix = np.zeros((self.width, self.height, 2), dtype=np.uint8)
		pix[..., 0] = np.add(np.bitwise_and(img[..., 0], 0xF8), np.right_shift(img[..., 1], 5))
		pix[..., 1] = np.add(np.bitwise_and(np.left_shift(img[..., 1], 3), 0xE0), np.right_shift(img[..., 2], 3))
		pix = pix.flatten().tolist()
		
		# Set LCD window to full screen
		self.set_display_area_position_size(0, 0, self.width, self.height)
		self.digital_write(self.GPIO_DC_PIN, True)
		
		# Write pixel data to LCD
		for i in range(0, len(pix), 4096):
			self.spi_writebyte(pix[i:i + 4096])