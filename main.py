import random
import copy
import time
import pygame
import sys

#importing pygame output code
import pg_output as pgo


class Game:
	def __init__(self, field_size=6, block_size=5):
		"""
		generating random symmetric field/array
		True is "living cell" False is dead.
		There is an extra False at the end and an extra line of false at the bottom
		This ensures that the borders are handeld correctly when accessing the array
		"""
		self.size = field_size
		
		self.field = [[False if row == field_size else bool(random.getrandbits(1)) \
						for row in range(0, field_size+1)] \
						for line in range(0, self.size)]
		self.field.append([False for i in range(0, self.size+1)]) #adding extra row of False

		self.mult_sqare = pgo.MultiSquare(self.field, screen, size=block_size) #builder for pygame input



	def count(self):
		"""
		This part iterates trough the array for each row and every object in that row
		For every object in the row it will access the nine fields around that object
		and counts the Trues and Falses around that object
		This data will be stored in a simple dict as a number mapped to True and False
		"""
		self.new_line = [] #this is used in analyze() to store the new lines objects
		self.new_field = [] #also used in analyze() it will contain the final new arry
		for y in range(0, self.size):
			for x in range(0, self.size):
				#[y][x] - cursurs trough whole field, handels each item
				
				#contains the current object - needed for its staus in analyze()
				self.current_cell = self.field[y][x] 
				#print(f"Main: {self.current_cell}")
				#dict which contains the counts - resetted after every object
				self.counter_dict = {
					True: 0,
					False: 0
				}

				#"circling" around one object (3x3 block)
				#adding -1, 0 and 1 to the coordinates of objects y and x axis to move around it
				for h in range(-1, 2): #y axis
					for v in range(-1, 2): #x axis
						# yv = y + v
						# xh = x + h
						if h == 0 and v == 0: #center - object itself
							pass
						else:
							self.counter_dict[self.field[y+v][x+h]] += 1
							#print(self.field[y+v][x+h])
				#print(self.counter_dict)
				
				#calling analyze to get the new cells status from the collected data
				self.analyze()

		#when every object was accessed this part ensures that there will be the False line below
		#and that new_field is copied to field correctly
		self.new_field.append([False for i in range(0, self.size+1)])
		self.field = copy.deepcopy(self.new_field)
		# for row in self.new_field:
		# 	print(row)

	def analyze(self):
		"""
		This block analyzed the data from the dict created in count()
		It will append the new status to new_line
		When line conatins a full row a False object will be added
		and it will be appended to new_field and be reset
		"""

		#current cell is alive and has not enough neigbours -> dies
		if self.counter_dict[True] > 3 or self.counter_dict[True] < 2:
			self.new_line.append(False)
			#print("died")

		#living cell has enough neigbours to stay alive
		elif (self.current_cell == True and self.counter_dict[True] == 2) or self.counter_dict[True] == 3:
			self.new_line.append(True)
			#print("allive")

		else: #nothing special happened to the cell -> remains its status
			self.new_line.append(self.current_cell)

		#print(f"len {len(self.new_line)}, line: {self.new_line}")

		#check if row is full
		if len(self.new_line) == self.size:
			self.new_line.append(False) #safety false
			self.new_field.append(self.new_line) #adding line to field
			self.new_line = [] #resetting
			#print(self.new_field)

		#print()
	

	def output(self, field=None):
		"""
		The function responsible for the output
		-> Produces a string
		"""
		
		#comment in if you want to pass in an other field in
		#also rename "self.field" in the first loop to "grid"
		#if field:
		#	grid = field
		#else:
		#	grid = self.field
		
		self.field_str = ""
		#simple double loop to acess each item of a nested list
		for line in self.field:
			for pos in line:
				if pos == True: #alive
					#self.field_str += "😃"
					self.field_str += "■ "
				else:			#dead
					#self.field_str += "  "
					self.field_str += "  " #❏
			self.field_str += "\n" #break after full line
		print(chr(27) + "[2J")
		print(self.field_str)

	def pygame_output(self, screen):

		self.mult_sqare.prod(self.field)
		self.mult_sqare.update()



#cxecuting the whole thing
if __name__ == "__main__":
	
	##SETTINGS##

	#True keeps the block size by 5 and scales the windows around it - better for large numbers
	#False scales the blocks to fit into a 1080x1080 grid - better for smaller numbers
	objects = 120
	block_size = 10
	scale_window_fixed_blocks = True


	if scale_window_fixed_blocks == True:
		#objects +2 because because we have a gap from 2 between the block
		#block_size +2 because of the space between objects
		#plus block_size because 1:1 and noch 0:0 is used as startpoint (times 2 for symmetry)
		win_size = (objects) * (block_size + 2) + block_size * 2

	else:
		win_size = 1080
		block_size = 1080 / (objects) - 2
		block_size = int(block_size)
		print(block_size)

	#Building the Window
	#flags = pygame.OPENGL | pygame.RESIZABLE
	flags = pygame.RESIZABLE #| pygame.NOFRAME
	screen = pygame.display.set_mode((win_size, win_size), flags)

	pygame.display.set_caption("Game of life")

	pygame.display.flip() #activating window
	game = Game(objects, block_size=block_size)

	while True:
		for event in pygame.event.get():
		 	if event.type == pygame.QUIT:
		 		sys.exit("Closed by user")

		
		game.pygame_output(screen)
		game.count()
		#time.sleep(0.05) #timer - ensures a more stable framerate
		#game.output() #old terminal output







