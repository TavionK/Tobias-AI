import datetime
# Tobias Class file
class Tobias:
	name = "Tobias"
	version = 0.4
	mk = 2
	location = "Fredericksburg"
	creator = "Tavion Britt"
	bday = datetime.datetime(2023,5,15)

# Init method
	def __init__(self):
		pass

# Returns the name "Tobias"
	def getName(self):
		return self.name

# Returns the version (2.0, 2.2, etc.)
	def getVersion(self):
		return self.version

# Returns the mk
	def getMk(self):
		return self.mk 

# Returns the location
	def getLoc(self):
		return self.location

# Returns the Creator
	def getCreator(self):
		return self.creator

# Returns birthday
	def getBday(self):
		return self.bday.strftime("%B %d, %Y")

# Returns age
	def getAge(self):
		# calculate years (does take into account the month)
		years = datetime.datetime.today().year - self.bday.year - ((datetime.datetime.today().month, datetime.datetime.today().day) <= (self.bday.month, self.bday.day))

		# calculate months of age
		if datetime.datetime.today().month <= self.bday.month:
			months = self.bday.month - datetime.datetime.today().month
		else:
			months = datetime.datetime.today().month - self.bday.month

		# if less than a month and a year calculate the days
		if years < 1 and months < 1:
			days = self.bday.day - datetime.datetime.today().day
			return str(days) + " days old"
		# calculate age if under a year but over a month
		elif years < 1 and months >= 1:
			return str(months) + " months old"
		# calculate years and months if year is over over 1
		else:
			return str(years) + " years old"

# t = Tobias()
# print(t.getAge())