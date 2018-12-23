class Human:

	# Static variable (private)
	__total = 0;

	# Constructor & Overloading
	def __init__(self,name=None):
		if name is not None:
			# Attribute
			self.name = name
		else:
			self.name = ""	
		Human.__total+=1
	
	# Static method	
	@staticmethod
	def human_cry():
		print("QQ")

	# Class method like staticmethod but use class as firs parameter
	@classmethod
	def human_total(cls):
		print(str(cls.__total)+" people")

	# Method
	def say_name(self):
		if self.name:
			print("My name is "+self.name)
		else: 
			print("i don't hava a name")	


## Inheritance
class Male(Human):


	def __init__(self,name=None):
		super(Male, self).__init__(name)

	## Override
	def say_name(self):
		print("I am a man, my name is "+self.name)

## Inheritance
class Female(Human):
	
	def __init__(self,name=None):
		super(Female, self).__init__(name)

	## Override
	def say_name(self):
		print("I am a woman, my name is "+self.name)		




if __name__ == '__main__':
	
	human1 = Human()
	human2 = Human("John")
	human1.say_name()
	human2.say_name()
	Human.human_cry()
	Human.human_total()
	print("=============")
	human3 = Male("Bob")
	human4 = Female("Amy")
	
	## Polymorphism
	for human in [human1,human2,human3,human4]:
		human.say_name()
	Human.human_total()

	