class Fish:
	def __init__(self, name='Denise',hunger=0,happiness = 10):
		self.name = name 
		self.hunger = hunger
		self.happiness = happiness

		# add 4 other data fields 

	def eat(self):
		self.hunger= self.hunger - 1
		self.happiness = self.happiness + 1
		print(self.name +" has eaten")
		# what happens hunger and happiness when the fish eats?

	def swim(self):
		self.hunger = self.hunger + 1
		self.happiness = self.happiness +1
		print(self.name +" is swimming")
		# what happens to hunger and happiness when the fist swims?

	#what other things does the fish do besides eat and swim?
fish = Fish()