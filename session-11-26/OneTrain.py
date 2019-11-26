class OneTrain():
	def __init__(self,direction='North',current_position='SouthFerry'):
		self.stops = ['SouthFerry','Rector','WTC Cortlandt','Chambers',
		'Franklin','Canal','Houston','Christopher','14','18','23',
		'28','34','42','59','66','72','79','86','96','103','116',
		'125','137','145','157','168','181','191','Dyckman','207'
		'215','225','231','238','242']
		self.direction=direction

		self.current_position = current_position


	def next_stop(self):
		current_stop = self.current_position
		stops = self.stops
		index = stops.index(current_stop)
		if not self.turn_around():
			new_index = 0
			if self.direction == 'North':
				new_index = index+1
			elif self.direction == 'South':
				new_index = index-1
			self.current_position= self.stops[new_index]
		self.make_announcement(self.current_position)



	def turn_around(self):
		stop = self.current_position
		direction = self.direction
		if stop == 'SouthFerry' and direction=='South':
			self.direction = 'North'
			self.current_position = 'Rector'
		elif stop == '242' and direction == 'North':
			self.direction = 'South'
			self.current_position = '238'
		else:
			return False


	def make_announcement(self, next_stop):
		direction = self.direction
		print("This is a "+direction+"bound 1 train. The next stop is "+next_stop)


Train = OneTrain()
Train.next_stop()
Train.next_stop()
Train.next_stop()

		

