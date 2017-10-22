def name(func):

	def inner(*args, **kwargs):
		print('Running this method:', func.__name__)
		return func(*args, **kwargs)

	return inner


class CoffeeMachine:

	WATER_LEVEL = 100

	@name
	def _start_machine(self):
		if self.WATER_LEVEL > 20:
			return True
		else:
			print("Please add water")
			return False

	@name
	def __boil_water(self):
		return "Boiling water..."

	@name
	def make_coffee(self):
		if self._start_machine():
			self.WATER_LEVEL -= 20
			print(self.__boil_water())
			print("Coffee ready!")


machine = CoffeeMachine()

for _ in range(6):
	machine.make_coffee()


machine.make_coffee()
machine._start_machine()
machine._CoffeeMachine__boil_water() # access private method from outside the class