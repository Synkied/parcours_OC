# coding: utf-8

def e_t(func):
	def inner():
		print("Maison... Téléphone... Maison...")
		return func()
	return inner

@e_t
def gertie():
	print("Je lui ai appris à parler ! Écoute !")


@e_t
def elliott():
	print("Il veut rentrer chez lui !")



elliott()
gertie()
