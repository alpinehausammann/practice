#!/usr/bin/python
import random

class mapc:
	
	def __init__(self):
		#self.x = x
		#self.y = y
		self.course = []
		
	def genCourse(self, x, y):
		
		for i in range(x+1):
			for a in range(y+1):
				self.course.append((i,a))
		return self.course
	
	def startLocationGen(self, course):
		return random.sample(course, 10)
		

class sprites:
	
	def __init__(self, typeSprite, randomLocation):
		self.typeSprite = typeSprite
		self.startLocation = randomLocation.pop()
		self.health = 0
		self.speed = 0
		self.attack = 0
		self.stats = {"sprite_type" : self.typeSprite, "starting_location" : self.startLocation}
		
	#def setStart(self):
	#	 self.stats['stating_location'] = self.randomLocation.pop()
		
	def setHealth(self):
		
		if self.typeSprite == 'user':
			self.health = 10
		
		self.stats['health'] = self.health
	
	def setSpeed(self):
		
		if self.typeSprite == 'user':
			self.speed = 2
		elif self.typeSprite == 'enemy':
			self.speed = 1
			
		self.stats['speed'] = self.speed
	
	def setAttack(self):
		
		if self.typeSprite == 'enemy':
			
			self.attack=1
		
		self.stats['attack'] = self.attack
		
	def createSprite(self):
		#self.setStart()
		self.setHealth()
		self.setSpeed()
		self.setAttack()
		return self.stats
course = mapc().genCourse(10,11)


starting_locations = mapc().startLocationGen(course)

player = sprites('user', starting_locations).createSprite()
monster = sprites('enemy', starting_locations).createSprite()
#player = player.setStart().setHealth().setSpeed().setAttack()
#player
#print(player.setHealth)

print(player)
print(monster)

