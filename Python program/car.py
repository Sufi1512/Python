# python-inheritance.py
class StudentDetails:
	'''Represents Company  Member.'''
	def __init__(self, name, roll_no, age):
		self.name = name
		self.roll_no = roll_no
		self.age = age
	def tell(self):
		'''Details of an Student.'''
		print('Name: ', self.name,'\nRollNo : ',self.roll_no, '\nAge : ',self.age)
