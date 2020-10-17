import pygame


class Changes:
	"""
	A class for object modifications, like color
	"""
	def __init__(self):
		self.red = 0
		self.green = 0
		self.blue = 0

	def rgb(self):
		"""
		A "cheap" rotation trough RGB colours 
		"""
		if self.red < 255:
			self.red += 1
		elif self.green < 255:
			self.green += 1
		elif self.blue < 255:
			self.blue += 1
		else:
			self.red = 0
			self.green = 0
			self.blue = 0
		#print(red)
		colour = (self.red, self.green, self.blue)
		#screen.fill(colour)
		return colour

class MultiSquare():
	"""
	Responsible for the generation of blocks from a True/False 'array'
	Requires at least a nested list as argument, must be symmetrical 
	-> lists in list = entries per list
	Lists must contain values that can be differentiated by True or False
	"""

	def __init__(self, array, x=1, y=1, size=30):


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
		

	def prod(self, colour=(255, 255, 255)):
		"""
		The actual production of the visual field
		"""

		# self.cases = {
		# 	True: pygame.draw.rect(screen, colour, self.rect),
		# 	False: pygame.draw.rect(screen, (0,0,0), self.rect)
		# 	}

		for y in range(0, len(self.array)):
			for x in range(0, len(self.array)):
				#setting new coordinates for the rectangle
				#start-coord * current pos in array * scale of a rectangle
				self.rect = ((self.x * ((x+1)*(self.size+2)), self.y * ((y+1)*(self.size+2))),self.sqare)
				obj = self.array[y][x] #accessing array entry
				
				#checking if Rectangle is color or black
				if obj:
					pygame.draw.rect(screen, colour, self.rect)
				else:
					pygame.draw.rect(screen, (0,0,0), self.rect)


if __name__ == "__main__":
	pygame.init()

	#Building the Window
	#flags = pygame.OPENGL | pygame.RESIZABLE
	flags = pygame.RESIZABLE
	screen = pygame.display.set_mode((1920, 1080), flags)

	pygame.display.set_caption("Game of life")

	pygame.display.flip() #activating window


	#test array
	array = [[True, True, True, True],
			[True, False, True, True],
			[True, True, True, True],
			[True, True, True, True]]

	mult_sq = MultiSquare(array) #init squares

	change = Changes() #init changes

	#main-loop
	while True:
		for event in pygame.event.get():
		 	if event.type == pygame.QUIT:
		 		pygame.quit()

		mult_sq.prod() #making squares

		pygame.display.update() #updating view






