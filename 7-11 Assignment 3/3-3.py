#Assignment 3-3
#parent class
class organism:
	
	def __init__(self, units_tax, units_name):
		self.units_tax = units_tax
		self.units_name = units_name
		
	
	def description(self):
		return 'Info: ' + self.units_tax + ' + ' + self.units_name

#new class
class longorganism(organism):
	
	def __init__(self, units_tax, units_name,region):
		organism.__init__(self, units_tax, units_name)
		self.region = region

	def newdescription(self):
		return 'Info: ' + self.units_tax + '+' + self.units_name + '+' + self.region
c2 = longorganism('tax1', 'Organism1','R1')
print(c2.newdescription())
