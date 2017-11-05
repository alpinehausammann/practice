class sprites:
#	def __init__(self,typeSprite):
#		self.typeSprite = typeSprite
	def __init__(self, typeSprite):
		self.typeSprite = typeSprite
		#self.startLocation = startLocation
		#self.health = health
		#self.speed = speed
		#self.attack = attack
		
	def setStart(self,randomLocation):
		return self.randomLocation.pop(random.choice(1))
		
	def setHealth(self, typeSprite):
		if self.typeSprite == 'user':
			health = 10
		else:
			health = None
		return health
	
	def setSpeed(self, typeSprite):
			if self.typeSprite == 'user':
				speed == 2
			elif typeSprite == 'enemy':
				speed == 1
			else:
				speed = None
			return speed
	
	def setAttack(self, typeSprite):
		if self.typeSprite == 'enemy':
			attack=1
			
		else:
			attack = None
		return attack

	def createDict(self, typeSprite):
		
		dict = {"type": self.typeSprite, "startLocation": sprites.setStart(start_locations), "health": sprites.setHealth(self.typeSprite), 
				"speed" : sprites.setSpeed(self.typeSprite), "attack": sprites.setAattack(self.typeSprite}
		return dict
