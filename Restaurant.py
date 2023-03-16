class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
	
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type.title()
		
		
	def describe_restaurant(self):
	
		print('The restaurant name is ....'+' '+str(self.restaurant_name))
		print('The cuisine type is ...'+' '+str(self.cuisine_type))
		
	
	def open_restaurant(self):
	
		print('The Restaurant is now open .... ')

class User():

	def __init__(self, last_name, first_name, password, username):
	
		self.last_name = last_name.title()
		self.first_name = first_name.title()
		self.password = password
		self.username = username
		self.company = 'BGLC'
		self.full_name = str(self.first_name)+' '+str(self.last_name)
		
		
	def describe_user(self):
	
		print('Your name is'+' '+self.full_name.title())
		print('\nand your password/username are'+' '+self.password+'/'+self.username)
		
	
	def greet_user(self):
	
		print('\nHello'+' '+self.full_name.title()+', '+'welcome to the '+str(self.company.title()))
		
		
restaurant = Restaurant('pagoda', 'italian')
jamaican = Restaurant('Rasta', 'vegetarian')
japanese = Restaurant('japaN', 'susHI')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.open_restaurant()

restaurant.describe_restaurant()

jamaican.describe_restaurant()

japanese.describe_restaurant()


employee = User('Thompson', 'CouRTney', 'CEST2000', 'cest2000')

employee.describe_user()
employee.greet_user()

