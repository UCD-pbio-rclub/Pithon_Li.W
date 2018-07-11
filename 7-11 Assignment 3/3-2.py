#Assignment 3-2
class organism:
	
	def __init__(self, units_tax, units_name,):
		self.units_tax = units_tax
		self.units_name = units_name
		
	
	def description(self):
		return 'Info: ' + self.units_tax + ' + ' + self.units_name

	

c1 = organism('KPCOFGS', 'Organism1')
print(c1.description())

