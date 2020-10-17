import pygame


class Changes:
	"""
	A class for object modifications, like color
	"""
	def __init__(self):
		self.red = 255
		self.green = 0
		self.blue = 0

	def rgb(self):
		"""
		A real implementation of RGB
		"""
		
		if self.red < 255 and self.green == 255:
			self.red += 5
			self.green -= 5
		elif self.red < 255 and self.green > 0 and self.blue == 0:
			self.red += 5
			self.green -= 5
		elif self.blue < 255 and self.red > 0:
			self.blue += 5
			self.red -= 5
		elif self.green < 255 and self.blue > 0:
			self.green += 5
			self.blue -= 5
		elif self.red < 255 and self.green > 0:
			self.red += 5
			self.blue -= 5

		colour = (self.red, self.green, self.blue)
		print(colour)
		#screen.fill(colour)
		return colour

	def cheap_rgb(self):
		"""
		A "cheap" interation trough RGB colours 
		"""
		if self.red < 255:
			self.red += 3
		elif self.blue < 255:
			self.blue += 3
		elif self.green < 255:
			self.green += 3
		else:
			self.red = 54
			self.green = 0
			self.blue = 0

		colour = (self.red, self.green, self.blue)
		print(colour)
		#screen.fill(colour)
		return colour
class MultiSquare():
	"""
	Responsible for the generation of blocks from a True/False 'array'
	Requires at least a nested list as argument, must be symmetrical 
	-> lists in list = entries per list
	Lists must contain values that can be differentiated by True or False
	"""

	def __init__(self, array, screen, x=1, y=1, size=5):

		self.screen = screen
		self.array = array

		#start values
		self.x = x 	#x pos
		self.y = y	#y pos
		self.position = (self.x, self.y) 
		self.size = size #size of a rectangle
		self.sqare = (size, size)
		self.colour = (255, 255, 255) #white
		self.thickness = 1
		#making a default rectanlge
		self.rect = ((self.x, self.y), self.sqare)

		self.changes = Changes()

		

	def prod(self, array, colour=(255, 255, 255)):
		"""
		The actual production of the visual field
		"""

		# self.cases = {
		# 	True: pygame.draw.rect(screen, colour, self.rect),
		# 	False: pygame.draw.rect(screen, (0,0,0), self.rect)
		# 	}
		self.array = array
		colour = self.changes.rgb()
		for y in range(0, len(self.array)):
			for x in range(0, len(self.array)):
				#setting new coordinates for the rectangle
				#start-coord * current pos in array * scale of a rectangle
				self.rect = ((self.x * ((x+1)*(self.size+2)), self.y * ((y+1)*(self.size+2))),self.sqare)
				obj = self.array[y][x] #accessing array entry
				
				#checking if Rectangle is color or black
				if obj:
					pygame.draw.rect(self.screen, colour, self.rect)
				else:
					pygame.draw.rect(self.screen, (0,0,0), self.rect)

	def update(self):
		pygame.display.update()



if __name__ == "__main__":
	pygame.init()

	#Building the Window
	#flags = pygame.OPENGL | pygame.RESIZABLE
	flags = pygame.RESIZABLE #| pygame.NOFRAME
	screen = pygame.display.set_mode((1080, 1080), flags)

	pygame.display.set_caption("Game of life")

	pygame.display.flip() #activating window

	#test array
	array = [[True, True, True, True],
			[True, False, True, True],
			[True, True, True, True],
			[True, True, True, True]]

	mult_sq = MultiSquare(array, screen) #init squares

	change = Changes() #init changes
	#main-loop
	while True:
		for event in pygame.event.get():
		 	if event.type == pygame.QUIT:
		 		pygame.quit()

		mult_sq.prod() #making squares

		pygame.display.update() #updating view






